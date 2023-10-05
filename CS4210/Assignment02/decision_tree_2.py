#-------------------------------------------------------------------------
# AUTHOR: Siddharth Kekre
# FILENAME: decision_tree_2.py
# SPECIFICATION: Decision Tree 2 Code
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:
    dbTraining = []
    X = []
    Y = []
    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)
    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    for data in dbTraining:
        feature_vector = []
        for i in range(4):
            if data[i] == 'Young':
                feature_vector.append(1)
            elif data[i] == 'Prepresbyopic':
                feature_vector.append(2)
            elif data[i] == 'Presbyopic':
                feature_vector.append(3)
            elif data[i] == 'Myope':
                feature_vector.append(1)
            elif data[i] == 'Hypermetrope':
                feature_vector.append(2)
            elif data[i] == 'Yes':
                feature_vector.append(1)
            elif data[i] == 'No':
                feature_vector.append(2)
            elif data[i] == 'Normal':
                feature_vector.append(1)
            elif data[i] == 'Reduced':
                feature_vector.append(2)
        X.append(feature_vector)
    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    for data in dbTraining:
        if data[4] == 'Yes':
            Y.append(1)
        elif data[4] == 'No':
            Y.append(2)
    #loop your training and test tasks 10 times here
    accuracy_sum = 0
    for i in range (10):
       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)
       #read the test data and add this data to dbTest
       #--> add your Python code here
        dbTest = []
        #reading the test data in a csv file
        with open('contact_lens_test.csv', 'r') as testfile:
            reader = csv.reader(testfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)
       correct_predictions = 0
       for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            feature_vector = []
            for i in range(4):
                if data[i] == 'Young':
                    feature_vector.append(1)
                elif data[i] == 'Prepresbyopic':
                    feature_vector.append(2)
                elif data[i] == 'Presbyopic':
                    feature_vector.append(3)
                elif data[i] == 'Myope':
                    feature_vector.append(1)
                elif data[i] == 'Hypermetrope':
                    feature_vector.append(2)
                elif data[i] == 'Yes':
                    feature_vector.append(1)
                elif data[i] == 'No':
                    feature_vector.append(2)
                elif data[i] == 'Normal':
                    feature_vector.append(1)
                elif data[i] == 'Reduced':
                    feature_vector.append(2)
            class_predicted = clf.predict([feature_vector])[0]
           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            if class_predicted == 1 and data[4] == 'Yes':
                correct_predictions += 1
            elif class_predicted == 2 and data[4] == 'No':
                correct_predictions += 1
        accuracy = correct_predictions / len(dbTest)
        accuracy_sum += accuracy
    #find the average of this model during the 10 runs (training and test set)
    average_accuracy = accuracy_sum / 10
    #print the average accuracy of this model during the 10 runs (training and test set).
    print("Final accuracy when training on {}: {}".format(ds, average_accuracy))