#-------------------------------------------------------------------------
# AUTHOR: Siddharth Kekre
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #3
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/
#IMPORTANT NOTE: YOU HAVE TO WORK WITH THE PYTHON LIBRARIES numpy AND pandas to complete this code.

#importing some Python libraries
from sklearn import svm
import numpy as np
import pandas as pd

#defining the hyperparameter values
c = [1, 5, 10, 100]
degree = [1, 2, 3]
kernel = ["linear", "poly", "rbf"]
decision_function_shape = ["ovo", "ovr"]

#reading the training data by using Pandas library
df = pd.read_csv('optdigits.tra', sep=',', header=None)
#getting the first 64 fields to create the feature training data and convert them to NumPy array
X_training = np.array(df.values)[:, :64]
#getting the last field to create the class training data and convert them to NumPy array
y_training = np.array(df.values)[:, -1]

#reading the testing data by using Pandas library
df = pd.read_csv('optdigits.tes', sep=',', header=None)
#getting the first 64 fields to create the feature testing data and convert them to NumPy array
X_test = np.array(df.values)[:, :64]
#getting the last field to create the class testing data and convert them to NumPy array
y_test = np.array(df.values)[:, -1]

#created 4 nested for loops that will iterate through the values of c, degree, kernel, and decision_function_shape

highest_accuracy = 0
best_parameters = ()

for c_val in c:
    for degree_val in degree:
        for kernel_val in kernel:
            for decision_function_shape_val in decision_function_shape:
                
                # Creating an SVM classifier 
                clf = svm.SVC(C=c_val, degree=degree_val, kernel=kernel_val, decision_function_shape=decision_function_shape_val)
                
                # Fitting SVM to the training data
                clf.fit(X_training, y_training)
                
                correct_predictions = 0 
                # Making predictions for each test sample
                for (x_testSample, y_testSample) in zip(X_test, y_test):
                    prediction = clf.predict([x_testSample])
                    if prediction == y_testSample: 
                        correct_predictions += 1 

                accuracy = correct_predictions/len(y_test)
                
                # Checking if accuracy is higher than previous highest accuracy
                if accuracy > highest_accuracy:
                    highest_accuracy = accuracy
                    best_parameters = (c_val, degree_val, kernel_val, decision_function_shape_val)

print(f"Highest SVM accuracy so far: {highest_accuracy}, Parameters: C={best_parameters[0]}, degree={best_parameters[1]}, kernel={best_parameters[2]}, decision_function_shape={best_parameters[3]}")
