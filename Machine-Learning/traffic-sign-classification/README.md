Introduction:  
Traffic sign recognition is a lucrative real-world problem which we have chosen to address due to its high practical relevance, especially in the context of its application in transportation. Traffic signs are designed to catch the eye of a human driver and be easily recognized. They usually follow a standard design, shape and color to aid accurate recognition. However, many real-world factors such as weather conditions, lighting in the environment and field of view might come into play; often leading to the drivers being misguided. There may also be instances when the human drivers may be unable to interpret the signs due to lack of knowledge. This can be mitigated using machine learning algorithms to accurately classify images of traffic signs, which could ultimately be used to prompt the drivers with clear instructions pertinent to the traffic signs. This capability can also be extrapolated to autonomous vehicles. To achieve level-5 autonomous, accurate classification would help the vehicles understand and follow traffic rules.  

Problem Statement:  
The aim of this project is to read and classify traffic signs from multiple images of traffic signs captured from different ranges of lighting, distances and resolutions. We aim to improve get the best accuracy for specific signs like “warning” or “danger”, due to their nature of impact. We aim to interpret if specific features in an image like shape, color etc plays an important role in accurate classification of the groups. There are several different types of traffic signs like speed limits, no entry, traffic signals, turn left or right, children crossing, no passing of heavy vehicles, etc. These different classes of Traffic signs are grouped into 6 overarching categories and the classification modelling is performed to identifying the group of a traffic sign recognised by a car cam.  

Data Source:  
https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign

Methodology:  
Our methodology to building this traffic sign classification model can be broken down into five steps. This is a brief outline of the methodology. Each section will be elaborated in detail further in the report.  
1. Exploratory data analysis  
a. Understanding the distribution of traffic sign classes, sign shapes and image resolutions.  
b. Performing Principal component analysis to identify the patterns for grouping  
c. Grouping similar traffic signs into 6 subsets Speed, Prohibitory, De-restriction, Mandatory, Danger and Other based on the geometric shapes and structures as identified in the PCA  

2. Data pre-processing  
	a. Scaling and resizing of images.  
	b. Down Sampling of data (depending on the modelling algorithm applied). 
  
3. Training and evaluating 5 classification models:   
a. Random Forest   
b. Multi-Layer Perceptron Neural networks  
c. Kernel SVM   
d. KNN Classifier and   
e. Linear Discriminant Analysis   

4. Selecting the best performing model using validation dataset based on the evaluation metrics decided   
5. Reporting the performance of selected model using a test set and interpreting the results by comparing against the human performance in identifying the traffic signs.  


Exploratory Data Analysis Quick View:  
Traffic sign image classes used for classification.  
![Snapshot of Classes](https://github.com/gmadhu89/academic-projects/blob/main/Machine-Learning/traffic-sign-classification/traffic-classes.jpg?raw=true "Snapshot of Classes")

Distribution of Images.  
![Snapshot of Images](https://github.com/gmadhu89/academic-projects/blob/main/Machine-Learning/traffic-sign-classification/dist-images.jpg?raw=true "Snapshot of Images")

Distribution of Pixels.  
![Snapshot of Pixels](https://github.com/gmadhu89/academic-projects/blob/main/Machine-Learning/traffic-sign-classification/dist-pixels.jpg?raw=true "Snapshot of Pixels")


