#-------------------------------------------------------------------------
# AUTHOR: Siddharth Kekre
# FOR: CS 4210- Assignment #4
#-----------------------------------------------------------*/

# Importing Necessary Libraries
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier 
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

n = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
r = [True, False]

# Reading Training Dataset as Pandas Dataframe
df = pd.read_csv('optdigits.tra', sep=',', header=None) 

X_training = np.array(df.values)[:,:64] # Training Features
y_training = np.array(df.values)[:,-1]  # Training Labels

# Reading Testing Dataset as Pandas Dataframe
df = pd.read_csv('optdigits.tes', sep=',', header=None)

X_test = np.array(df.values)[:,:64] # Testing Features
y_test = np.array(df.values)[:,-1]  # Testing Labels

# Initializing Evaluation Metrics as 0
highest_accuracy = {'Perceptron': 0, 'MLP': 0}
best_params = {'Perceptron': {}, 'MLP': {}}

for learning_rate in n: #iterates over n

    for shuffle in r: #iterates over r

        # Iterates over Both Algorithms
        for algorithm in ['Perceptron', 'MLP']:

            # Create a Neural Network classifier
            if algorithm == 'Perceptron':
                clf = Perceptron(eta0=learning_rate, shuffle=shuffle, max_iter=1000)
            else:
                clf = MLPClassifier(activation='logistic', learning_rate_init=learning_rate, hidden_layer_sizes=(25,), shuffle=shuffle, max_iter=1000)

            # Fit the Neural Network to the Training Data
            clf.fit(X_training, y_training)

            # Prediction for Each Test Sample to Compute Accuracy
            predictions = clf.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)

            # If the Calculated Accuracy is Higher than Previously Calculated, Update the Highest Accuracy
            if accuracy > highest_accuracy[algorithm]:
                highest_accuracy[algorithm] = accuracy
                best_params[algorithm] = {'learning_rate': learning_rate, 'shuffle': shuffle}
                print(f'Highest {algorithm} accuracy so far: {accuracy}, Parameters: learning rate={learning_rate}, shuffle={shuffle}')


