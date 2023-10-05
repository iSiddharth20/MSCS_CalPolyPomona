#-------------------------------------------------------------------------
# AUTHOR: Siddharth Kekre
# FILENAME: naive_bayes.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB

#reading the training data in a csv file
data = []
with open('Assignment 2/weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header
    for row in reader:
        data.append(row[1:])  # Ignoring the Day column
#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
feature_mapping = {'Sunny': 1, 'Overcast': 2, 'Rain': 3, 'Hot': 1, 'Mild': 2, 'Cool': 3, 'High': 1, 'Normal': 2, 'Weak': 1, 'Strong': 2}
X = [[feature_mapping[feature] for feature in row[:-1]] for row in data]
#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
class_mapping = {'Yes': 1, 'No': 0}
Y = [class_mapping[row[-1]] for row in data]
#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)
#reading the test data in a csv file
test_data = []
with open('Assignment 2/weather_test.csv', 'r') as testfile:
    reader = csv.reader(testfile)
    next(reader) # skip header
    for row in reader:
        test_data.append(row[1:])  # Ignoring the Day column
#printing the header os the solution
print("Probability1,Probability2,Classification")
#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
for row in test_data:
    test_sample = [feature_mapping[feature] for feature in row[:-1]]
    prob = clf.predict_proba([test_sample])[0]
    classification = 'None'
    if max(prob) >= 0.75:
        classification = 'Yes' if clf.predict([test_sample])[0] == 1 else 'No'
    print(f"{prob[0]:.2f},{prob[1]:.2f},{classification}")