#!/usr/bin/env python
# coding: utf-8

# Importing required libraries
import csv
import pandas as pd
import numpy as np
from PIL import Image
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from random import shuffle
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


# Getting review files
genre_files_list = ['Design_Illustration_review.csv','Adventure_review.csv','Casual_review.csv','Simulation_review.csv',
'Sports_review.csv','Massively_Multiplayer_review.csv','Racing_review.csv','Free_to_Play_review.csv',
'RPG_review.csv','Strategy_review.csv','Early_Access_review.csv','Photo_Editing_review.csv','Indie_review.csv','Animation_Modeling_review.csv','Utilities_review.csv']


#genre_files = [genre_files_list[0]]
#genre_files = [genre_files_list[2]]
#genre_files = [genre_files_list[1]]
#genre_files = [genre_files_list[3]]
#genre_files = [genre_files_list[4]]
#genre_files = [genre_files_list[5]]
#genre_files = [genre_files_list[6]]
#genre_files = [genre_files_list[7]]
#genre_files = [genre_files_list[8]]
#genre_files = [genre_files_list[9]]
#genre_files = [genre_files_list[10]]
#genre_files = [genre_files_list[11]]
#genre_files = [genre_files_list[12]]
#genre_files = [genre_files_list[13]]
#genre_files = [genre_files_list[14]]
#genre_files = ['Action_review.csv']


# Initializing lists to hold the sentiment data for each genre
g = globals()
for i in genre_files:
    j = i[:-4]
    if '&' in j:
        j = j.replace("&","")
    lst_name = 'genre_{}'.format(j)
    g['genre_{}'.format(j)] = []

    with open(i,'r',encoding="utf8") as sentiment:
        print(i)
        reader = csv.reader(sentiment, delimiter=',')
        for row in reader:
            g['genre_{}'.format(j)].append(row)


sentiment_data.head()

## Generating word clouds of positive reviews
for i in genre_files:
    j = i[:-4]

    print('genre_{}'.format(j))
    sentiment_data = g['genre_{}'.format(j)]

    header = sentiment_data[0]
    data = sentiment_data[1:]

    df = pd.DataFrame(data,columns=header)
    df = sentiment_data

    df_positive = df[df['sentiment'] == 'positive']

    words_p = list(df_positive['review'])

    words_p_filtered = []

    stop_words = set(stopwords.words('english'))
    more_stopwords = {'one', 'br', 'Po', 'th', 'sayi', 'fo', 'Unknown'}
    stop_words = stop_words.union(more_stopwords)

    #stop_words = set(stopwords.words('english'))
    words_to_be_removed = ['penis','fuck','booby','Porn','fucking','ass','porn','sex']
    ps = PorterStemmer()

    for word in words_p:
        tokens = word_tokenize(word)
        words_p_filtered.append(''.join([ps.stem(w.strip()) for w in tokens if not w in stop_words and not w.lower() in words_to_be_removed]))

    words_p_str = pd.Series(words_p_filtered).str.cat(sep=' ')

    wordcloud_p = WordCloud(width=1600, height=800,stopwords = stop_words, max_font_size=200,background_color='white',max_words = 1000,colormap="Blues").generate(words_p_str)

    filename = 'genre_{}'.format(j) + str('_wc_positive.png')

    wordcloud_p.to_file(filename)


comments_text = words_p_str
comments_mask = np.array(Image.open('comment.png'))
plot_wordcloud(comments_text,filename, comments_mask, max_words=400, max_font_size=120,
               title = 'Positive Comments', title_size=30,colormap='Blues',color="#9ab7d3")


def plot_wordcloud(text,filename, mask=None, max_words=800, max_font_size=180, figure_size=(24.0,16.0),
                   title = None, title_size=40, image_color=False,colormap='Blues',color=None):
    stopwords = set(stop_words)
    more_stopwords = {'one', 'br', 'Po', 'th', 'sayi', 'fo', 'Unknown','penis','fuck','booby','Porn','fucking','ass','porn','sex'}
    stopwords = stopwords.union(more_stopwords)

    wordcloud = WordCloud(background_color='white',
                    stopwords = stopwords,
                    max_words = max_words,
                    max_font_size = max_font_size,
                    random_state = 42,
                    mask = mask,
                    colormap=colormap)
    wordcloud.generate(text)

    wordcloud.to_file(filename)

    plt.figure(figsize=figure_size)
    if image_color:
        image_colors = ImageColorGenerator(mask);
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear");
        plt.title(title, fontdict={'size': title_size,
                                  'verticalalignment': 'bottom'})
    else:
        plt.imshow(wordcloud);
        plt.title(title, fontdict={'size': title_size, 'color': color,
                                  'verticalalignment': 'bottom'})
    plt.axis('off');
    plt.tight_layout()




