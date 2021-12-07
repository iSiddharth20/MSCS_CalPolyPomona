#!/usr/bin/python3

'''
Importing Necessary Libraries
'''
# Importing and Exporting Dataset
import pandas as pd


'''
Importing Data Formatting Functions from 'text_formatting.py'
'''
from text_formatting import format_data


'''
Importing the Original Dataset
Original Dataset Source :
https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews/version/1
'''
# Importing Original Dataset
data = pd.read_csv('Dataset/OriginalDataset.csv')


'''
Data Pre-Processing
'''
# Removing all the Null Values and Resetting Index of the Dataset
data.dropna(inplace=True)
data.reset_index(inplace=True)
data.drop(columns=['index'],axis=1,inplace=True)


'''
Data Cleaning and Updation
'''
lst = list(data['review'])
for i,v in enumerate(lst):
    lst[i] = format_data(v)
# Replacing Original Dataset with Cleaned Dataset
data = data.drop(columns=['review'])
data['Review'] = lst
data.rename(columns={"sentiment": "Sentiment"}, inplace = True)


'''
Exporting Cleaned Dataset as a CSV File
'''
data.to_csv('Dataset/CleanedData.csv', index=False)
