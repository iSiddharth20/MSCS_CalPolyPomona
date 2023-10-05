#-------------------------------------------------------------------------
# AUTHOR: Siddharth Kekre
# FILENAME: knn.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
# Initialize the error count
error_count = 0
#loop your data to allow each instance to be your test set
for test_index in range(len(db)):
    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    X = [list(map(float, db[i][:2])) for i in range(len(db)) if i != test_index]
    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    Y = [1 if db[i][2] == '+' else 0 for i in range(len(db)) if i != test_index]
    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = list(map(float, db[test_index][:2]))
    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)
    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    class_predicted = clf.predict([testSample])[0]
    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if (db[test_index][2] == '+' and class_predicted == 0) or (db[test_index][2] == '-' and class_predicted == 1):
        error_count += 1
#print the error rate
# Calculate the LOO-CV error rate
error_rate = error_count / len(db)
print("The leave-one-out cross-validation error rate for 1NN is:", error_rate)