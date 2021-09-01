This folder contains a classification task of spambase data by comparing CART Decision tree classifier and Random forest algorithm using scikit-learn. The steps followed are provided below:   

A spam classifier is built using the UCR email spam dataset https://archive.ics.uci.edu/ml/datasets/Spambase came from the postmaster and individuals who had filed spam. Data and documentation is available in /data/ folder. The collection of non-spam emails came from
filed work and personal emails, and hence the word 'george' and the area code '650' are indicators of non-spam. These are useful when constructing a personalized spam filter. Missing values are filled with zero.   

1. The classifier is first built using a CART (Classification and Regression Tree).  
2. A classifier is also constructed using Random Forest model. 
3. A one-class SVM approach for spam filtering is experimented. Data is randomly shuffled and partitioned to use 80% for training and the remaining 20% for testing. All non-spam emails are extracted from the training block (80% of data you have selected) to build the one-class kernel SVM using RBF kernel (you can turn the kernel bandwidth to achieve good performance). Then , it is applied on the 20% of data reserved for testing (thus this is a novelty detection situation). The total misclassification error rate on this testing data is then reported.   

CART_RandomForest.html - Contains results of the classification.  

** Source code will be provided upon request.**