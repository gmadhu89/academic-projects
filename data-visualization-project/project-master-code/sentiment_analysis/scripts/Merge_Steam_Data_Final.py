import csv
import pandas as pd
import numpy as np
from collections import defaultdict
import yaml


def read_files(filename):
    '''
    Function to read csv files and store return header + data as a tuple
    '''

    with open(filename,encoding="utf8") as csv_file:

        data = []

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count +=1
            else:
                data.append(row)
                line_count +=1
    return (header,data)

# Reading the data files in csv format for formatting and merging
data_steam_spy = read_files("steamspy_data.csv")
data_player_count = read_files("steam_player_count.csv")
data_steamapp = read_files("steam_app_data.csv")


# Creating a dataframe for the player counts data for further processing

app_id = []
response = []
for i in range(len(data_player_count[1])):
    response.append(yaml.load(data_player_count[1][i][0]))
    app_id.append(data_player_count[1][i][1])

player_count_df = pd.DataFrame({data_player_count[0][0]:response , data_player_count[0][1]:app_id})
player_split = player_count_df['response'].apply(pd.Series)
player_count_df = player_split.merge(player_count_df['app_id'].to_frame(),left_index=True, right_index=True)

# Creating a dataframe for the Steam Spy Data
d = defaultdict(list)
for i in range(len(data_steam_spy[1])):
    for j in zip(data_steam_spy[0], data_steam_spy[1][i]):
        d[j[0]].append(j[1])

steam_spy_df = pd.DataFrame(dict(d))

# Splitting the tags information from Steam Spy into columns and creating a final dataframe
tags = []

for i in range(len(data_steam_spy[1])):
    tags.append(yaml.load(data_steam_spy[1][i][19]))

tags_df = pd.DataFrame({'tags':tags})
tags_df = tags_df['tags'].apply(pd.Series)
tags_df = tags_df.replace(np.nan, 0)

## Merging the tags split with original dataset
steam_spy_without_tags = steam_spy_df.drop('tags',axis=1)
steam_spy_tags_split = steam_spy_without_tags.merge(tags_df,left_index=True, right_index=True)

## Dropping columns that are blank/ duplicated in Steamapp data
steam_spy_tags_split.drop(['score_rank','userscore','price','initialprice','discount','genre'],axis=1,inplace=True)

## Creating a DataFrame with Steam App Data

d = defaultdict(list)
for i in range(len(data_steamapp[1])):
    for j in zip(data_steamapp[0], data_steamapp[1][i]):
        d[j[0]].append(j[1])

steam_app_df = pd.DataFrame(dict(d))


## Transforming the platforms column to dictionary to split it approporiately
platforms_new = []
for row in steam_app_df["platforms"]:
    if row == '':
        platforms_new.append({'windows':'','mac':'','linux':''})
    else:
        platforms_new.append(yaml.load(row))

steam_app_df['platforms'] = platforms_new

## Transforming the price_overview column to dictionary to split it approporiately
price_new = []
for row_p in steam_app_df["price_overview"]:
    if row_p == '':
        price_new.append({'currency':'','initial':'','final':'','discount_percent':'','initial_formatted':'','final_formatted':''})
    else:
        price_new.append(yaml.load(row_p))

steam_app_df['price_overview'] = price_new

## Transforming the price_overview column to dictionary to split it approporiately
metacritic = []
for row_m in steam_app_df['metacritic']:
    if row_m == '':
        metacritic.append('')
    else:
        metacritic.append(yaml.load(row_m)['score'])

steam_app_df['metacritic'] = metacritic


## Transforming the recommendations column to hold only the value
recommendations = []
for row in steam_app_df['recommendations']:
    if row == '':
        recommendations.append('')
    else:
        recommendations.append(yaml.load(row)['total'])

steam_app_df['recommendations'] = recommendations

## Transforming the Release Date column to hold only the date

release_date = []
for row in steam_app_df['release_date']:
    if row == '':
        release_date.append('')
    else:
        release_date.append(yaml.load(row)['date'])

steam_app_df['release_date'] = release_date


## Splitting the genres information into columns to represent multiple genres for a single game
import ast
genres = []
for row in steam_app_df["genres"]:
    if row == '':
        genres.append([{}])
    else:
        genres_per_app = defaultdict(int)
        for d in ast.literal_eval(row):
            genres_per_app[d['description']] += 1
        genres.append(dict(genres_per_app))

steam_app_df['genres'] = genres

genres_split = steam_app_df['genres'].apply(pd.Series)
genres_split = genres_split.replace(np.nan,0)

## Merging the genres split with original dataset
steam_app_without_genre = steam_app_df.drop('genres',axis=1)
steam_app_df = steam_app_without_genre.merge(genres_split,left_index=True, right_index=True)

## Splitting the platforms and price to columns
platform_split = steam_app_df['platforms'].apply(pd.Series)
price_split = steam_app_df['price_overview'].apply(pd.Series)

## Merging with final dataframe
steam_app_final = steam_app_df.merge(platform_split,left_index=True,right_index=True)
steam_app_final = steam_app_final.merge(price_split,left_index=True,right_index=True)

#Removing the original price and platform columns
steam_app_final.drop(['price_overview','platforms'],axis=1,inplace=True)

# Dropping columns that are not required (either fully blank or duplicated with steam spy)
steam_app_final.columns
steam_app_final.drop(['controller_support','pc_requirements','mac_requirements','linux_requirements','screenshots','movies'],axis=1,inplace=True)


#Merging all three sources of data into a single dataframe to be exported
steam_final = steam_app_final.merge(steam_spy_df, how='inner', left_on = ['steam_appid'],right_on=['appid'])
steam_final = steam_final.merge(player_count_df,how='inner', left_on = ['steam_appid'],right_on = ['app_id'])

steam_final.drop(['appid','app_id','result'],axis=1,inplace=True)
steam_final.drop([0],axis=1,inplace=True)
steam_final.drop(['name_y'],axis=1,inplace=True)


# Exporting data to csv file
steam_final.to_csv('steam_data_final.csv',index=False)
