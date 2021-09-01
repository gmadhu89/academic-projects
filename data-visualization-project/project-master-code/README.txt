                                      CSE 6242 TEAM 10 PROJECT OVERVIEW AND DEMO INSTRUCTIONS

README.txt             : File with summary of project and steps to access visualization
Folder (CODE):
App/                   : Code base for the web application and visualization
ML/                    : Code base for Machine learning models
sentiment_analysis/    : Code base for Sentiment Analysis/ text processing
  
                                              PROJECT OVERVIEW / DESCRIPTION
Our goal is to use machine learning models to predict new games’ success rate in the current market. Our project targets benefiting game companies in increasing their profits by leveraging machine learning techniques on the vast amount of data available. We will present our results in an interactive interface through visualization. To officially define the objective of this project, we will propose a methodology that utilizes the historical data available at main-stream game databases to establish various machine learning models, which are used to estimate the success rate of new products and design new games that can achieve high investment returns in the current market. We also analyze user reviews from textual data and provide visualization of user feedback to gain more insights on popular game features. An interactive user interface has been created to give audience more convenience to access the research outputs. 

                                              ###  INSTALLATION STEPS ###
Install the below components in your machine:
1) Python V3 or above
2) Run the below commands in command line/ terminal.
pip install python-dotenv
pip install statsmodels
3) Download the Code Zip file (or clone from Github repository : https://github.gatech.edu/sbalogun6/CSE-6242-Project) to your local.
                                              
                                              ###  EXECUTION STEPS  ###
For optimal performance, machine learning models are pretrained and word clouds are generated for each genre. The visualization pulls data from a flask backend via RESTful calls. Follow the below steps to execute and view the visualization.

1. In command line, navigate to folder CSE-6242-Project/App
2. Type "flask run" and press enter
3. Copy the url printed (https://127.0.0.1:5000/) in the command line and paste it into your browser to run it
You 

If you run into an error, you may try the following:
## Retrain the ML models locally if needed
4. In command line, navigate to CSE-6242-Project/App/playtime_pred
5. Type "python3 Playtime_Prediction_ML.py" 
6. Retry the three steps(1-3) for running the demo.

                                                ### DATA ###
The datasets to run the models are available in the code base. User review dataset is very large, and the source link is provided below:
# User Reviews
https://www.kaggle.com/najzeko/steam-reviews-2021
# Steam Video Game Hours Played
We could then attach genre/rating/developer to the user play on [games mentioned](https://data.world/quanticdata/steam-video-game-hours-played/discuss/steam-video-game-hours-played/grrtaoby)

## Steam API
How steam has been used, [num of download](https://steamspy.com/about)

## Video Game Sales with Ratings
How game sales related to [ratings](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings)
