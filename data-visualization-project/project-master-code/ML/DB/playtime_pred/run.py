# load the model from disk
import pickle
import sys

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def predict_regional_playtime(genre, rating, platform, price):
    # load pre-trained regressors
    filename_NA = './NA_playtime.sav'
    filename_EU = './EU_playtime.sav'
    filename_JP = './JP_playtime.sav'
    filename_Other = './Other_playtime.sav'
    loaded_model_NA = pickle.load(open(filename_NA, 'rb'))
    loaded_model_EU = pickle.load(open(filename_EU, 'rb'))
    loaded_model_JP = pickle.load(open(filename_JP, 'rb'))
    loaded_model_Other = pickle.load(open(filename_Other, 'rb'))

    # set up the conversion of the input values into the vector format
    df = pd.read_csv('./playtime_ML.csv')
    df.drop(columns=['country_code'], inplace=True)
    df = df[['Genre', 'ESRB_Rating', 'Platform', 'price', 'NA_playtime']]
    X = df.iloc[:, :-1].values
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 1, 2])], remainder='passthrough')

    # convert the design inputs]
    ct.fit(X)
    design = [[genre, rating, platform, price]]
    X_ds = ct.transform(design).toarray()

    # make prediction
    y_pred_NA = loaded_model_NA.predict(X_ds)
    y_pred_EU = loaded_model_EU.predict(X_ds)
    y_pred_JP = loaded_model_JP.predict(X_ds)
    y_pred_Other = loaded_model_Other.predict(X_ds)

    # output is a list of predicted playtime at the four regions regarding the design
    output_pred = [y_pred_NA[0], y_pred_EU[0], y_pred_JP[0], y_pred_Other[0]]

    return output_pred


if __name__ == '__main__':
    # design inputs come from the system call
    genre = sys.argv[1]
    rating = sys.argv[2]
    platform = sys.argv[3]
    price = sys.argv[4]

    # calling the prediction function
    output = predict_regional_playtime(genre, rating, platform, price)
    print('[{northamerica:.2f},{eu:.2f},{jp:.2f},{other:.2f}]'.format(northamerica=output[0], eu=output[1],
                                                                     jp=output[2], other=output[3]))
