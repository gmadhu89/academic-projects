import csv
import numpy as np  # http://www.numpy.org
import ast
from datetime import datetime
from math import log, floor, ceil
import random
import numpy as np

class Utility(object):

    # This method computes entropy for information gain
    def entropy(self, class_y):
        # Input:
        #   class_y         : list of class labels (0's and 1's)

        # TODO: Compute the entropy for a list of classes
        #
        # Example:
        #    entropy([0,0,0,1,1,1,1,1,1]) = 0.918 (rounded to three decimal places)

        entropy = 0
        ### Implement your code here
        #############################################

        # class_y: type : numpy array

        import math
        # Lets us keep 1's as class a and 0's as class b
        p_a = class_y.count(1)/len(class_y)
        p_b = class_y.count(0)/len(class_y)

        # Calculating entropy
        if p_a != 0.0 and p_b != 0.0:
            entropy = round(-p_a*math.log(p_a,2) -p_b*math.log(p_b,2),3)

        if p_a == 0.0 and p_b != 0.0:
            entropy = round(p_a -p_b*math.log(p_b,2),3)

        if p_a != 0.0 and p_b == 0.0:
            entropy = round(-p_a*math.log(p_a,2) +p_b,3)

        if p_a == 0.0 and p_b == 0.0:
            entropy = 0.0
        #############################################
        return entropy


    def partition_classes(self, X, y, split_attribute, split_val):
        # Inputs:
        #   X               : data containing all attributes
        #   y               : labels
        #   split_attribute : column index of the attribute to split on
        #   split_val       : a numerical value to divide the split_attribute



        # TODO: Partition the data(X) and labels(y) based on the split value - BINARY SPLIT.
        #
        # Split_val should be a numerical value
        # For example, your split_val could be the mean of the values of split_attribute
        #
        # You can perform the partition in the following way
        # Numeric Split Attribute:
        #   Split the data X into two lists(X_left and X_right) where the first list has all
        #   the rows where the split attribute is less than or equal to the split value, and the
        #   second list has all the rows where the split attribute is greater than the split
        #   value. Also create two lists(y_left and y_right) with the corresponding y labels.



        '''
        Example:



        X = [[3, 10],                 y = [1,
             [1, 22],                      1,
             [2, 28],                      0,
             [5, 32],                      0,
             [4, 32]]                      1]



        Here, columns 0 and 1 represent numeric attributes.



        Consider the case where we call the function with split_attribute = 0 and split_val = 3 (mean of column 0)
        Then we divide X into two lists - X_left, where column 0 is <= 3  and X_right, where column 0 is > 3.



        X_left = [[3, 10],                 y_left = [1,
                  [1, 22],                           1,
                  [2, 28]]                           0]



        X_right = [[5, 32],                y_right = [0,
                   [4, 32]]                           1]



        '''
        #X : type : numpy array
        #y : type : numpy array

        #X_left = []
        #X_right = []

        #y_left = []
        #y_right = []
        ### Implement your code here
        #############################################

        X = np.array(X)
        y = np.array(y)

        X_left = X[X[:,split_attribute] <= split_val]
        X_right = X[X[:,split_attribute] > split_val]

        #y_left = y[np.where((X == X_left[:,None]).all(-1))[1]]
        #y_left = y[np.where(np.all(X == X_left,axis=1))]
        #y_right = y[np.where((X == X_right[:,None]).all(-1))[1]]

        y_left = y[X[:,split_attribute] <= split_val]
        y_right = y[X[:,split_attribute] > split_val]

        #############################################
        return [X_left, X_right, y_left,y_right]


    def information_gain(self, previous_y, current_y):
        # Inputs:
        #   previous_y: the distribution of original labels (0's and 1's)
        #   current_y:  the distribution of labels after splitting based on a particular
        #               split attribute and split value

        # TODO: Compute and return the information gain from partitioning the previous_y labels
        # into the current_y labels.
        # You will need to use the entropy function above to compute information gain
        # Reference: http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15381-s06/www/DTs.pdf

        """
        Example:

        previous_y = [0,0,0,1,1,1]
        current_y = [[0,0], [1,1,1,0]]

        info_gain = 0.45915
        """

        info_gain = 0
        ### Implement your code here
        #############################################

        # previous_y : type : list
        # current_y  : type : list

        if previous_y == current_y:
            return 0
        else:
            H_L = self.entropy(current_y[0])
            H_R = self.entropy(current_y[1])
            H =   self.entropy(previous_y)
            P_L = len(current_y[0])/len(previous_y)
            P_R = len(current_y[1])/len(previous_y)

            info_gain = round(H - ((H_L * P_L) + (H_R * P_R)),5)
        #############################################
        return info_gain


    def best_split(self, X, y, f_ids=[]):
        # Inputs:
        #   X       : Data containing all attributes
        #   y       : labels
        #   TODO    : For each node find the best split criteria and return the split attribute,
        #             spliting value along with  X_left, X_right, y_left, y_right (using partition_classes)
        #             in the dictionary format {'split_attribute':split_attribute, 'split_val':split_val,
        #             'X_left':X_left, 'X_right':X_right, 'y_left':y_left, 'y_right':y_right, 'info_gain':info_gain}
        '''

        Example:

        X = [[3, 10],                 y = [1,
             [1, 22],                      1,
             [2, 28],                      0,
             [5, 32],                      0,
             [4, 32]]                      1]

        Starting entropy: 0.971

        Calculate information gain at splits: (In this example, we are testing all values in an
        attribute as a potential split value, but you can experiment with different values in your implementation)

        feature 0:  -->    split_val = 1  -->  info_gain = 0.17
                           split_val = 2  -->  info_gain = 0.01997
                           split_val = 3  -->  info_gain = 0.01997
                           split_val = 4  -->  info_gain = 0.32
                           split_val = 5  -->  info_gain = 0

                           best info_gain = 0.32, best split_val = 4


        feature 1:  -->    split_val = 10  -->  info_gain = 0.17
                           split_val = 22  -->  info_gain = 0.41997
                           split_val = 28  -->  info_gain = 0.01997
                           split_val = 32  -->  info_gain = 0

                           best info_gain = 0.4199, best split_val = 22


       best_split_feature: 1
       best_split_val: 22

       'X_left': [[3, 10], [1, 22]]
       'X_right': [[2, 28],[5, 32], [4, 32]]

       'y_left': [1, 1]
       'y_right': [0, 0, 1]
        '''

        # X:type : numpy array
        # y:type : numpy array

        if not isinstance(X,np.ndarray):
            X = np.array(X)
        if not isinstance(y,np.ndarray):
            y = np.array(y)

        best_split_attr = 0
        best_split_val = 0
        from collections import defaultdict
        from operator import itemgetter
        #X_left, X_right, y_left, y_right = [], [], [], []
        ### Implement your code here
        #############################################
        # Initializing a dictionary that will hold the value with max info gain per feature(column)
        IG_dict = defaultdict(lambda: defaultdict(list))
        attr_ind_map = {}

        H_start = self.entropy(list(y))

        ## Start iterating for every feature(column) in the data set
        if f_ids == []:
            for attr in range(X.shape[1]):
                IG_dict[attr] = []
                result = []

                for val in range(X.shape[0]):
                    X_L, X_R, y_L, y_R = self.partition_classes(X,y,attr,X[val][attr])
                    if list(y_L) == []:
                        current_y = list(y_R)
                    elif list(y_R) == []:
                        current_y = list(y_L)
                    else:
                        current_y = [list(y_L), list(y_R)]

                    IG = self.information_gain(list(y), current_y)
                    result.append([X[val][attr],IG])
                IG_dict[attr].append(sorted(result, key=itemgetter(1), reverse=True)[0])

        else:
            for ind,attr in enumerate(f_ids):
                attr_ind_map[attr] = ind
                IG_dict[attr] = []
                result = []
            ## Getting a value to split on
                for val in range(X.shape[0]):
                    X_L, X_R, y_L, y_R = self.partition_classes(X,y,ind,X[val][ind])

                    if list(y_L) == []:
                        current_y = list(y_R)
                    elif list(y_R) == []:
                        current_y = list(y_L)
                    else:
                        current_y = [list(y_L), list(y_R)]

                    IG = self.information_gain(list(y), current_y)
                    result.append([X[val][ind],IG])

                IG_dict[attr].append(sorted(result, key=itemgetter(1), reverse=True)[0])

        best_split_tup = sorted(IG_dict.items(), key= lambda x: x[1], reverse =True)[0]
        best_split_attr = best_split_tup[0]
        best_split_val = best_split_tup[1][0][0]
        best_info_gain = best_split_tup[1][0][1]

        ## Getting the X and y values based on the best split
        if f_ids == []:
            X_left, X_right, y_left, y_right = self.partition_classes(X,y,best_split_attr,best_split_val)
        else:
            X_left, X_right, y_left, y_right = self.partition_classes(X,y,attr_ind_map[best_split_attr],best_split_val)

        return {'split_attribute':best_split_attr, 'split_val':best_split_val, 'X_left':X_left, 'X_right':X_right, 'y_left':y_left, 'y_right':y_right, 'info_gain':best_info_gain}

        #############################################

class DecisionTree(object):
    def __init__(self, max_depth):
        # Initializing the tree as an empty dictionary or list, as preferred
        self.tree = {}
        self.max_depth = max_depth
        self.f_ids_g = []

    def all_same(self,y):
        if list(y).count(y[0]) == len(y):
            return True
        else:
            return False

    def learn(self, X, y, par_node = {}, depth=0,info_gain=0.1):
        # TODO: Train the decision tree (self.tree) using the the sample X and labels y
        # You will have to make use of the functions in Utility class to train the tree

        # par_node is a parameter that is useful to pass additional information to call
        # the learn method recursively. Its not mandatory to use this parameter

        # Use the function best_split in Utility class to get the best split and
        # data corresponding to left and right child nodes

        # One possible way of implementing the tree:
        #    Each node in self.tree could be in the form of a dictionary:
        #       https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
        #    For example, a non-leaf node with two children can have a 'left' key and  a
        #    'right' key. You can add more keys which might help in classification
        #    (eg. split attribute and split value)
        ### Implement your code here
        #############################################

        # X:type : numpy array
        # y:type : numpy array

        if not isinstance(X,np.ndarray):
            X = np.array(X)
        if not isinstance(y,np.ndarray):
            y = np.array(y)

        if depth == 0:
            n_features = int(np.sqrt(X.shape[1]))
            f_ids = np.random.permutation(X.shape[1])[:n_features]
            self.f_ids_g = f_ids

            Xtree = X[:,self.f_ids_g]
            ytree = y
        else:
            Xtree = X
            ytree = y

        # Base case 1: Stop building tree when there is no par_node defined
        if par_node is None:
            return None

        # Base case 2: Stop splitting tree when there are no labels
        elif len(ytree) == 0:
            return {'value':random.randint(0, 1)}

        # Base case 3: Stop splitting tree when we have a pure leaf node
        elif self.all_same(ytree):
            return {'value':ytree[0]}

        #Base case 4: Stop splitting if info_gain=0 and return the mode of the label
        elif info_gain == 0:
            return {'value':max(ytree, key=list(ytree).count)}

        # Base case 5: Stop splitting if max_depth has reached, and return mode of the label
        elif depth > self.max_depth:
            return {'value':max(ytree, key=list(ytree).count)}

        # Recursively build decision tree and update par_node with the values
        else:
            split_res = Utility().best_split(Xtree,ytree,self.f_ids_g)

            par_node = {"split_attribute":split_res['split_attribute'],"split_value":split_res['split_val'],"info_gain":split_res['info_gain']}
            par_node['left'] = self.learn(split_res['X_left'],split_res['y_left'],{},depth+1, split_res['info_gain'])
            par_node['right'] = self.learn(split_res['X_right'],split_res['y_right'],{},depth+1, split_res['info_gain'])

            #Incrementing the depth since we built a layer of the tree
            depth += 1

            self.tree = par_node
            return par_node

        #############################################

    def classify(self, record):
        # TODO: classify the record using self.tree and return the predicted label
        ### Implement your code here
        #############################################

        # record :type = list

        ref = self.tree

        while ref.get('left'):
            if record[ref['split_attribute']] <= ref['split_value']:
                ref = ref.get('left')
            else:
                ref = ref.get('right')
        return ref['value']

        #############################################

# This starter code does not run. You will have to add your changes and
# turn in code that runs properly.

"""
Here,
1. X is assumed to be a matrix with n rows and d columns where n is the
number of total records and d is the number of features of each record.
2. y is assumed to be a vector of labels of length n.
3. XX is similar to X, except that XX also contains the data label for each
record.
"""

"""
This skeleton is provided to help you implement the assignment.You must
implement the existing functions as necessary. You may add new functions
as long as they are called from within the given classes.

VERY IMPORTANT!
Do NOT change the signature of the given functions.
Do NOT change any part of the main function APART from the forest_size parameter.
"""


class RandomForest(object):
    num_trees = 0
    decision_trees = []

    # the bootstrapping datasets for trees
    # bootstraps_datasets is a list of lists, where each list in bootstraps_datasets is a bootstrapped dataset.
    bootstraps_datasets = []

    # the true class labels, corresponding to records in the bootstrapping datasets
    # bootstraps_labels is a list of lists, where the 'i'th list contains the labels corresponding to records in
    # the 'i'th bootstrapped dataset.
    bootstraps_labels = []

    def __init__(self, num_trees):
        # Initialization done here
        self.num_trees = num_trees
        self.decision_trees = [DecisionTree(max_depth=10) for i in range(num_trees)]
        self.bootstraps_datasets = []
        self.bootstraps_labels = []

    def _bootstrapping(self, XX, n):
        # Reference: https://en.wikipedia.org/wiki/Bootstrapping_(statistics)
        #
        # TODO: Create a sample dataset of size n by sampling with replacement
        #       from the original dataset XX.
        # Note that you would also need to record the corresponding class labels
        # for the sampled records for training purposes.

        sample = [] # sampled dataset
        labels = []  # class labels for the sampled records
        ### Implement your code here
        #############################################

        #Converting to a numpy array
        XX_arr = np.array(XX)
        #Extracting labels from the dataset
        y_arr = XX_arr[:,-1]
        #Extracting the features
        X_arr = XX_arr[:,0:8]

        # Getting random indexes to choose for bootstrap sampling of data (rows)
        idx = np.random.choice(range(len(y_arr)),size=len(y_arr))
        sample_rows = X_arr[idx]
        label_rows = y_arr[idx]

        # Getting random features from the dataset (sqrt of total number of features)
        #n_features = int(np.sqrt(X_arr.shape[1]))
        #f_ids = np.random.permutation(X_arr.shape[1])[:n_features]

        #sample.append(sample_rows[:,f_ids])
        #labels.append(label_rows[:,f_ids])

        sample.append(sample_rows)
        labels.append(label_rows)
        #############################################
        return (sample, labels)

    def bootstrapping(self, XX):
        # Initializing the bootstap datasets for each tree
        for i in range(self.num_trees):
            data_sample, data_label = self._bootstrapping(XX, len(XX))
            self.bootstraps_datasets.append(data_sample)
            self.bootstraps_labels.append(data_label)

    def fitting(self):
        # TODO: Train `num_trees` decision trees using the bootstraps datasets
        # and labels by calling the learn function from your DecisionTree class.
        ### Implement your code here
        #############################################

        for i in range(self.num_trees):
            self.decision_trees[i].learn(list(self.bootstraps_datasets[i][0]), list(self.bootstraps_labels[i][0]),{},depth=0,info_gain=0.1)
        #############################################

    def voting(self, X):
        y = []

        for record in X:
            # Following steps have been performed here:
            #   1. Find the set of trees that consider the record as an
            #      out-of-bag sample.
            #   2. Predict the label using each of the above found trees.
            #   3. Use majority vote to find the final label for this recod.
            votes = []

            for i in range(len(self.bootstraps_datasets)):
                dataset = self.bootstraps_datasets[i]

                if record not in dataset[0]:
                    OOB_tree = self.decision_trees[i]
                    effective_vote = OOB_tree.classify(record)
                    votes.append(effective_vote)

            counts = np.bincount(votes)

            if len(counts) == 0:
                # TODO: Special case
                #  Handle the case where the record is not an out-of-bag sample
                #  for any of the trees.
                # NOTE - you can add few lines of codes above (but inside voting) to make this work
                ### Implement your code here
                #############################################

                for i in range(len(self.bootstraps_datasets)):
                    dataset = self.bootstraps_datasets[i]
                    OOB_tree = self.decision_trees[i]
                    effective_vote = OOB_tree.classify(record)

                    votes.append(effective_vote)

                cnts = np.bincount(votes)
                y = np.append(y, np.argmax(cnts))
                #############################################
            else:
                y = np.append(y, np.argmax(counts))

        return y

    def user(self):
        """
        :return: string
        """
        ### Implement your code here
        #############################################
        return 'mganesan7'
        #############################################


# TODO: Determine the forest size according to your implementation.
# This function will be used by the autograder to set your forest size during testing
# VERY IMPORTANT: Minimum forest_size should be 10
def get_forest_size():
    forest_size = 10
    return forest_size

# TODO: Determine random seed to set for reproducibility
# This function will be used by the autograder to set the random seed to obtain the same results you achieve locally
def get_random_seed():
    random_seed = 0
    return random_seed
