import pandas as pd
from textblob import TextBlob
import logging
from pathlib import Path

def big_df_processing(file):

    df_chunk = pd.read_csv(file, chunksize=10000000)

    chunk_list = []
    for chunk in df_chunk:
        chunk_list.append(chunk)

    df_concat = pd.concat(chunk_list)

    return df_concat

def get_eng_reviews(file_path):

    df_chunk = pd.read_csv(file_path, chunksize=10000000)

    chunk_list = []
    for chunk in df_chunk:
        chunk_list.append(chunk)

    df_concat = pd.concat(chunk_list)

    df_filtered = df_concat[df_concat['language'] == "english"]

    return df_filtered

def review_sentiment(review):
    analysis = TextBlob(review)

    if analysis.sentiment.polarity > 0:
            return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def check_file_path(file_path):

    my_file = Path(file_path)
    if my_file.is_file():
        return True
    else:
        return False

def main():

    log = logging.getLogger('SentimentdataLog')

    file_path = "../data/steam_reviews.csv" #7GB of data
    eng_reviews_file = "../../data/eng_reviews.csv"

    #write code for checking if eng_reviews is present or not

    if not check_file_path(eng_reviews_file):

        log.info("eng_reviews.csv does not exist, generating file....")
        df_concat = big_df_processing(file_path) #Only for initial cleaning, don't run if eng_reviews.csv exists
        df = df_concat[df_concat['language'] == "english"]

    df = big_df_processing(eng_reviews_file)

    print(df.columns)

    df = df[['app_id', 'app_name', 'review_id',
       'language', 'review', 'recommended', 'votes_helpful', 'votes_funny', 'weighted_vote_score',
       'comment_count', 'steam_purchase', 'received_for_free',
       'written_during_early_access',]]

    df.dropna(subset=['app_id','app_name','review_id','review'], inplace=True)
    df.drop_duplicates(inplace=True)

    log.info("Generating sentiment...")
    df['sentiment'] = df['review'].apply(review_sentiment)

    df.to_csv("../output/final_review_data.txt", sep="\t", index=False)

    log.info("Getting count info...")
    #getting sentiment count
    sentiment_count = df_concat.groupby(by=["app_id","app_name","sentiment"]).count()
    sentiment_count.to_csv("../output/sentiment_count.txt",sep="\t")

if __name__ == '__main__':
    main()
