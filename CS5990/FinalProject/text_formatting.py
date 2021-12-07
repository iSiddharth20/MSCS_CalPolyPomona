#!/usr/bin/python3

'''
Importing Data Cleaning Functions from 'clean_data.py'
'''
from clean_data import strip_html_tags, remove_special_characters, remove_accented_chars, remove_stopwords, lemmatize_text


'''
Data Cleaning and Updation
'''
def format_data(review):
    # Remove HTML Tags
    review = strip_html_tags(review)
    # Remove Accented Characters
    review = remove_accented_chars(review)
    # Remove Special Characters
    review = remove_special_characters(review)
    # Remove English Stop Words
    review = remove_stopwords(review)
    # Lemmatise Text
    review = lemmatize_text(review)
    return review

def distributed_format(review):
    formatted_data = {}
    for word in review.split(' '):
        formatted_data[word] = True
    return formatted_data
