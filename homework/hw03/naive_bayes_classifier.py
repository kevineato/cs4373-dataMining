# Kevin Wilson syx009
import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

df = pd.read_csv('hwk03-02.csv')

# pipeline => vectorize dict input => Multinomial Naive Bayes classifier
pipe = make_pipeline(DictVectorizer(), MultinomialNB())

# data from csv used to train model
train_X = df[['department', 'age', 'salary']].to_dict('records')
train_y = df['status']

# fit model to training data
pipe.fit(train_X, train_y)

# get user input for prediction
print('Enter tuple for Naive Bayes in this format: DEPARTMENT AGE SALARY')
query_str = input('>> ')
print()

# split input on space and build dict from split
query = query_str.split(' ')
tup_dict = {'department': query[0], 'age': query[1], 'salary': query[2]}

# get prediction from user input as dict
pred = pipe.predict(tup_dict)

# print user input and result predicted by model
print('Naive Bayes Prediction of {}:'.format(tup_dict))
print(pred[0])

