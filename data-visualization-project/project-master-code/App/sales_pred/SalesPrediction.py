#!/usr/bin/python

import sys
import numpy as np
from statsmodels.iolib.smpickle import load_pickle

'''
First argument is region choice are [na jp pal other]
Second argument is how many year since release [0 - 100]
Third argument is expected rating [0 - 10]
Fourth argument is boolean whehter the game is from the top rated publisher or not. Careful the boolean is case sensitive [True False]
'''

def predict_sales(region, year_since_release, expected_rating, is_top_publisher):
    new_results = load_pickle("./sales_pred/%s_sales_possion_model.pickle" % region)

    df_arbitray_value = np.array(
        [float(year_since_release), float(expected_rating), is_top_publisher == "True"]
    )

    prediction = new_results.predict(df_arbitray_value)
    return prediction.tolist()

def predict_all_sales(expected_rating, is_top_publisher):
    top_publisher = is_top_publisher == "True"
    rating = float(expected_rating)

    prediction = {}
    for region in ["jp", "na", "other"]:
        model = load_pickle("./sales_pred/%s_sales_possion_model.pickle" % region)
        sales_list = []
        for year_since_release in range(21):
            input_vals = np.array([float(year_since_release), rating, top_publisher])
            sales_list.append(model.predict(input_vals)[0])

        prediction[region] = sales_list

    return prediction