This folder contains an analysis done on a dataset (about participants who completed the personal information form and a divorce pre- dictors scale). The data is a modified version of the publicly available at https://archive.ics.uci.edu/ml/datasets/Divorce+Predictors+data+set (by injecting noise so you will not get the exactly same results as on UCI website). The dataset marriage.csv is contained in the data/ folder. There are 170 participants and 54 attributes (or predictor variables) that are all real-valued. The last column of the CSV file is label y (1 means "divorce", 0 means "no divorce"). Each column is for one feature (predictor variable), and each row is a sample (participant). A detailed explanation for each feature (predictor variable) can be found at the website link above. Our goal is to build a classifier using training data, such that given a test sample, we can classify (or essentially predict) whether its label is 0 ("no divorce") or 1 ("divorce"). We are going to compare the following classifiers (Naive Bayes, Logistic Regression, and KNN).   I will use the first 80% data for training and the remaining 20% for testing.  

Second part of analysis was done on MNIST dataset to classify hand-written digit images. KNN, logistic regression, SVM, kernel SVM, and neural networks were implemented and performance of each classifier was compared. 