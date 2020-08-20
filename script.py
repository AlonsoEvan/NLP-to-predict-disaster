import process
import process2

import pandas as pd
import time
import nltk
import re
import string
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from nltk.corpus import stopwords
from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer
from collections import defaultdict
from collections import  Counter
plt.style.use('ggplot')
stop=set(stopwords.words('english'))
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

from nltk.stem.snowball import EnglishStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import f1_score

import joblib


train= pd.read_csv('train.csv')
test=pd.read_csv('test.csv')


# stop_words = set(stopwords.words('english'))
# tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
# stemmer = EnglishStemmer()
# lemmatizer = WordNetLemmatizer()


train['clean_text'] = train['text'].apply(lambda x : process.clean_text(x))

train['clean_text'] = train['clean_text'].apply(lambda x : process2.clean(x))


uniqueWordFrequents = {}
for tweet in train['clean_text']:
    for word in tweet.split():
        if(word in uniqueWordFrequents.keys()):
            uniqueWordFrequents[word] += 1
        else:
            uniqueWordFrequents[word] = 1
            

uniqueWordFrequents = pd.DataFrame.from_dict(uniqueWordFrequents,orient='index',columns=['Word Frequent'])
uniqueWordFrequents.sort_values(by=['Word Frequent'], inplace=True, ascending=False)

counVec = CountVectorizer(max_features = uniqueWordFrequents.shape[0])
bagOfWords = counVec.fit_transform(train['clean_text']).toarray()


X = bagOfWords
y = train['target']
print("X shape = ",X.shape)
print("y shape = ",y.shape)


start_time = time.time()

LR = LogisticRegression(penalty='l2', 
                                        solver='saga', 
                                        random_state = 55)  

LR.fit(X,y)

final_time = (time.time()- start_time)/60
print(f'The time in minutes: {final_time}')

joblib.dump(LR,'LR.joblib')

#If you want to predict, you could pass any data you want, you juste need to preprocess her before :) like this

'''
DataToPred = pd.read_csv('datatopred.csv')

DataToPred['clean_text'] = DataToPred['text'].apply(lambda x : process.clean_text(x))
DataToPred['clean_text'] = DataToPred['clean_text'].apply(lambda x : process2.clean(x))

uniqueWordFrequents = {}
for tweet in test['clean_text']:
    for word in tweet.split():
        if(word in uniqueWordFrequents.keys()):
            uniqueWordFrequents[word] += 1
        else:
            uniqueWordFrequents[word] = 1
            
#Convert dictionary to dataFrame
uniqueWordFrequents = pd.DataFrame.from_dict(uniqueWordFrequents,orient='index',columns=['Word Frequent'])
uniqueWordFrequents.sort_values(by=['Word Frequent'], inplace=True, ascending=False)

counVec = CountVectorizer(max_features = uniqueWordFrequents.shape[0])
bagOfWords = counVec.fit_transform(DataToPred['clean_text']).toarray()

predictions = LR.predict(bagOfWords)

predictions.to_csv("predictions.csv", index=False)
'''



















