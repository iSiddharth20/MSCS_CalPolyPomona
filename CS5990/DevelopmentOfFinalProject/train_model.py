#!/usr/bin/python3

'''
Importing Necessary Libraries
'''
# Basic Libraries
import pandas as pd
import random
# Training Model
import nltk
# Export Trained Model as *.pkl
import joblib


'''
Importing Data Cleaning Functions from 'clean_data.py'
'''
from text_formatting import distributed_format


'''
Importing the Dataset
'''
# Importing Original Dataset
data = pd.read_csv('Dataset/CleanedData.csv')


'''
Getting Cleaned Data in the Following Format
[( {'Word':True , 'Word':True} , 'Positive' ) , ( {'Word':True , 'Word':True} , 'Negative' )]
'''

# Formatting All the Positive Reviews
df_pos = data[data['Sentiment']=='positive']
positive_words = []
for sentence in list(df_pos['Review']):
    positive_words.append((distributed_format(sentence),'Positive'))
# Formatting All the Negative Reviews
df_neg = data[data['Sentiment']=='negative']
negative_words = []
for sentence in list(df_neg['Review']):
    positive_words.append((distributed_format(sentence),'Negative'))
# Combining the Positive and Negative Formatted Reviews
final_data = positive_words + negative_words


'''
Randomly shuffling the Dataset so as to create Unbaised Dataset
'''
random.shuffle(final_data)


# '''
# Splitting the Data in 80:20 Ration for Training:Testing
# '''
# train_data = final_data[:(int(0.8*len(final_data))-1)]
# test_data = final_data[int(0.8*len(final_data)):]
# '''
# Training the Model with 'Naive Bayes Classifier'
# '''
# model = nltk.classify.NaiveBayesClassifier.train(train_data)


'''
Using Entire Dataset as Movie Reviews as Users will enter New Reviews.
Having Entire Dataset to be used for Training, increases chances for Higher Accuracy.
Training the Model with 'Naive Bayes Classifier'
'''
model = nltk.classify.NaiveBayesClassifier.train(final_data)


'''
Exporting the Trained Model
'''
joblib.dump(model,"trained_model.pkl")
