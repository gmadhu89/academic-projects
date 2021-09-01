if __name__ == '__main__':
    import numpy as np
    import pandas as pd

    df = pd.read_csv('./../../DB/playtime_pred/playtime_ML.csv')

    df.drop(columns=['country_code'], inplace=True)

    df = df[['Genre', 'ESRB_Rating', 'Platform', 'price', 'NA_playtime']]

    df["ESRB_Rating"].unique()

    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    from sklearn.impute import SimpleImputer

    imputer = SimpleImputer(missing_values=np.nan, strategy='median')
    imputer.fit(X[:, 3:4])
    X[:, 3:4] = imputer.transform(X[:, 3:4])

    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder

    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 1, 2])], remainder='passthrough')
    X = ct.fit_transform(X).toarray()

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    from sklearn.tree import DecisionTreeRegressor

    dt_regressor = DecisionTreeRegressor(random_state=0)
    dt_regressor.fit(X, y)

    y_pred = dt_regressor.predict(X_test)
    np.set_printoptions(precision=2)
    # print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

    from sklearn.metrics import r2_score

    r2_score(y_test, y_pred)

    # Random forest

    # In[16]:

    from sklearn.ensemble import RandomForestRegressor

    rf_regressor = RandomForestRegressor(n_estimators=128, random_state=0)
    rf_regressor.fit(X, y)

    # In[17]:

    y_pred = rf_regressor.predict(X_test)
    np.set_printoptions(precision=2)
    # print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

    # In[18]:

    r2_score(y_test, y_pred)

    # In[19]:

    # accurracies = cross_val_score(estimator=rf_regressor, X=X_train, y=y_train, cv=10)
    # print("Accurracy: {:.2f} %".format(accurracies.mean()*100))
    # print("Standard Deviation: {:.2f} %".format(accurracies.std()*100))

    # from sklearn.model_selection import GridSearchCV
    #
    # parameters = [{'n_estimators': [2, 4, 8, 16, 32, 64, 128, 256, 512]}]
    # grid_search = GridSearchCV(estimator=rf_regressor,
    #                            param_grid=parameters,
    #                            scoring='r2',
    #                            cv=10,
    #                            n_jobs=-1)
    # grid_search.fit(X_train, y_train)
    # best_accuracy = grid_search.best_score_
    # best_parameters = grid_search.best_params_
    # # print('Best Accuracy: {:.2f} %'.format(best_accuracy*100))
    # print('Best Parameters:', best_parameters)

    # In[24]:

    # r2_score(y_test, y_pred)

    # Make prediction for any game design

    # In[26]:

    genre = 'Action-Adventure'
    rating = 'M'
    platform = 'X360'
    price = 1999.0
    design = [[genre, rating, platform, price]]
    X_ds = ct.transform(design).toarray()

    # In[27]:

    from sklearn.ensemble import RandomForestRegressor

    # NA model
    rf_regressor_NA = RandomForestRegressor(n_estimators=64, random_state=0)
    rf_regressor_NA.fit(X, y)
    # EU model
    rf_regressor_EU = RandomForestRegressor(n_estimators=64, random_state=0)
    df_all = pd.read_csv('./../../DB/playtime_pred/playtime_ML.csv')
    df_all.drop(columns=['country_code'], inplace=True)
    df = df_all[['Genre', 'ESRB_Rating', 'Platform', 'price', 'EU_playtime']]
    y = df.iloc[:, -1].values
    rf_regressor_EU.fit(X, y)
    # JP model
    rf_regressor_JP = RandomForestRegressor(n_estimators=64, random_state=0)
    df = df_all[['Genre', 'ESRB_Rating', 'Platform', 'price', 'JP_playtime']]
    y = df.iloc[:, -1].values
    rf_regressor_JP.fit(X, y)
    # Other model
    rf_regressor_Other = RandomForestRegressor(n_estimators=64, random_state=0)
    df = df_all[['Genre', 'ESRB_Rating', 'Platform', 'price', 'Other_playtime']]
    y = df.iloc[:, -1].values
    rf_regressor_Other.fit(X, y)

    # Save the model to disk
    import pickle

    filename_NA = './../../DB/playtime_pred/NA_playtime.sav'
    pickle.dump(rf_regressor_NA, open(filename_NA, 'wb'))
    filename_EU = './../../DB/playtime_pred/EU_playtime.sav'
    pickle.dump(rf_regressor_EU, open(filename_EU, 'wb'))
    filename_JP = './../../DB/playtime_pred/JP_playtime.sav'
    pickle.dump(rf_regressor_JP, open(filename_JP, 'wb'))
    filename_Other = './../../DB/playtime_pred/Other_playtime.sav'
    pickle.dump(rf_regressor_Other, open(filename_Other, 'wb'))

# # load the model from disk
# import pickle
#
# filename = 'D:/PhD VIII/CSE 6242/Proj_6242/CSE-6242-Project/DB/playtime_pred/NA_playtime.sav'
# loaded_model = pickle.load(open(filename, 'rb'))
#
# import pandas as pd
#
# df = pd.read_csv('D:/PhD VIII/CSE 6242/Proj_6242/CSE-6242-Project/DB/playtime_pred/playtime_ML.csv')
# df.drop(columns=['country_code'], inplace=True)
# df = df[['Genre', 'ESRB_Rating', 'Platform', 'price', 'NA_playtime']]
# X = df.iloc[:, :-1].values
#
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
#
# ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 1, 2])], remainder='passthrough')
#
# genre = 'Shooter'
# rating = 'E10'
# platform = 'PC'
# price = 0.0
#
# ct.fit(X)
# design = [[genre, rating, platform, price]]
# X_ds = ct.transform(design).toarray()
# y_pred = loaded_model.predict(X_ds)
#
# print("The playtime for genre {}, rating {}, platform {}, and price {} in North America is: {}".format(genre, rating,
#                                                                                                        platform, price,
#                                                                                                        y_pred[0]))
