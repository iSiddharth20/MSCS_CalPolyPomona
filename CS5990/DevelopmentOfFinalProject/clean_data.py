#!/usr/bin/python3

'''
Importing Necessary Libraries
'''
# Remove Known Noise from the Dataset
import re
import unicodedata
from bs4 import BeautifulSoup
# Work on 'Natural Language Processing'
import spacy
import nltk


'''
Initialising NLTK Tokeniser
'''
# Clean Movie Reviews by Tokenising them for Further Analysis
from nltk.tokenize.toktok import ToktokTokenizer
tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')
# Removing 'No' and 'Not' from Stopwords List
stopword_list.remove('no')
stopword_list.remove('not')


'''
Initiliasing Spacy Lemmatiser
'''
nlp = spacy.load('en_core_web_sm', disable=['ner'])
doc = nlp(u"I don't want parsed", disable=['parser','tag','entity'])


'''
Defining Functions for Cleaning of Data
'''
# Remove HTML Tags from Movie Reviews
def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text()
    return stripped_text

# Remove Special Characters
def remove_special_characters(text):
    text = re.sub('[^a-zA-z0-9\s]', '', text)
    return text

# Remove Accented Chracters from Movie Reviews
def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

# Remove Stop Words from Movie Reviews
def remove_stopwords(text, is_lower_case=False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text

# Lemmatization : Getting Words to their Base Form
def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text

