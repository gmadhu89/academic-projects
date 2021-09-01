###########################################################################################################
REGIONAL_PLAYTIME_PREDICTION
This code is used to train regressors for regional playtime, save models, and then load models to predict the playtime for various game designs.
This code is supposed to work under the directory structure of the Proj_6242 project, as all files needed for running the models have been placed to the right places under the structure.
###########################################################################################################


###########################################################################################################
Two steps for usage
In general, two steps are needed to use the prediction function:
----------------------------------------------------------------------------------------------------------------------------------------------
1. Training
Although pre-trained models are available in the directory, a user is still recommended to train the models by himself/herself since training and prediction must be done with the same Python and Scikit-learn versions and issues such as data type errors can occur otherwise.
To train the regressors, run the Playtime_Prediction_ML.py under Algo/playtime_training folder. This will train the regressors needed for prediction and pickle all the models as .sav files.
----------------------------------------------------------------------------------------------------------------------------------------------
2. Prediction
After successfully training the models, a user can use them to predict regional playtime for different game designs.
The "run.py" under directory "DB/playtime_pred" contains the function for prediction and also the main function which can take inputs from a system call, excecute the prediction function, and then print the results to the console. It is up to the user to use call "run.py" from terminal, or just use the prediction function within the file.

The prediction function takes in four parameters as the game design from the user. They are Genre, ESRB_Rating, Platform, and Price. The output of the function is a list of predicted playtime at four regions, in the order of North America, Europe, Japan, and Other.

Note that the options for the four parameters are limited as follows:

Genre:
['Fighting', 'Strategy', 'Adventure', 'Action', 'Role-Playing', 'Shooter', 'Platform', 'Action-Adventure', 'MMO', 'Puzzle', 'Sports', 'Racing', 'Simulation', 'Music', 'Misc']

ESRB_Rating:
['T', 'E10', 'M', 'RP', 'E']

Platform:
['PS3', 'X360', 'PC', 'PS4', 'NS', 'XOne', 'XBL', 'PSN', 'XB', 'PSV', '3DS', 'WiiU', 'And', 'OSX', 'Linux', 'WW', 'PS', 'SAT', 'NGage', 'iOS', 'PS2', 'DS', 'Wii', 'PSP', 'N64', 'DC', 'GB', 'DSiW', 'GBA']

Price:
A double variable between 0 and 5500 (in cents)
----------------------------------------------------------------------------------------------------------------------------------------------
###########################################################################################################