import pandas as pd
import logging
from pathlib import Path

def clean_genre_name(row):
    genre_name = row.lstrip().rstrip()
    return genre_name

def create_genre_txt(main_df, file_name, genre):

    df = main_df[main_df['genre_type'] == str(genre)]
    df.to_csv("../output/genre_data/"+file_name, sep="\t", index=False)

def check_file_path(file_path):

    my_file = Path(file_path)
    if my_file.is_file():
        return True
    else:
        return False

def main():

    log = logging.getLogger('GenredataLog')

    log.info("Checking for input files...")
    #code for checking if files exist

    steam_data_path = "../../data/steam_data_final.csv"
    review_data_path = "../../output/sentiment_data.csv"

    if check_file_path(steam_data_path) and check_file_path(review_data_path):

        steam_data = pd.read_csv(steam_data_path)
        steam_review = pd.read_csv(review_data_path)

        #Getting a list of steam ids for the data that we have
        steam_app_ids = steam_data['steam_appid'].tolist()
        steam_app_ids = list(set(steam_app_ids))

        #Removing rows depending on the app id
        flt_review = steam_review[steam_review.app_id.isin(steam_app_ids)]

        #Separating reviews based on different genres
        genre_data = steam_data[['steam_appid','genre']].drop_duplicates()
        genre_data.rename(columns={"steam_appid": "app_id"}, inplace=True)

        genre_review = pd.merge(flt_review, genre_data, how="left", on="app_id")

        genre_review = genre_review.assign(genre_type=genre_review['genre'].str.split(',')).explode('genre_type')

        genre_review['genre_type'] = genre_review['genre_type'].apply(clean_genre_name)

        genre_review.to_csv("../output/filtered_review_data.txt",sep="\t", index=False)

        genre_count = pd.DataFrame({'count' : genre_review.groupby( [ "genre_type",] ).size()}).reset_index()

        log.info("Separated review data based on genres")

        genre_count.to_csv("../output/genre_count.txt", sep="\t", index=False)

        log.info("Getting counts...")

        #getting counts
        genre_gamereview_counts = pd.DataFrame({'count' : genre_review.groupby( [ "app_id","app_name","genre_type","sentiment"] ).size()}).reset_index()
        genre_review_counts = pd.DataFrame({'count' : genre_review.groupby( [ "genre_type","sentiment"] ).size()}).reset_index()

        genre_review_counts.to_csv("../output/genre_review_counts.txt", sep="\t", index=False)
        genre_gamereview_counts.to_csv("../output/game_genre_sent_count.txt", sep="\t", index=False)

        #Creating different dataframes for all genres

        genre_review = genre_review[['app_id', 'app_name', 'review_id', 'language', 'review', 'recommended',
           'votes_helpful', 'votes_funny', 'weighted_vote_score','sentiment', 'genre', 'genre_type']]

        genre_review['genre_type'] = genre_review['genre_type'].apply(clean_genre_name)

        genres = genre_count['genre_type'].tolist()
        genres = list(set(genres))

        log.info("Creating different dataframes for all genres")
        for genre in genres:
            genre = genre.lstrip().rstrip()
            genre = genre.replace(" ", "_")
            log.info("Review Data Created for "+genre)
            filename = str(genre)+"_review.txt"
            create_genre_txt(genre_review,filename,genre)

    else:

        raise Exception("Input Files Don't Exist!")

if __name__ == '__main__':
    main()
