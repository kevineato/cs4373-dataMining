# Kevin Wilson syx009
import pandas as pd

from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier

def convert_age(val):
    if val < 21 or val > 50:
        raise ValueError("Age must be between 21 and 50 inclusive")
    elif val <= 25:
        return '21..25'
    elif val <= 30:
        return '26..30'
    elif val <= 35:
        return '31..35'
    elif val <= 40:
        return '36..40'
    elif val <= 45:
        return '41..45'
    else:
        return '46..50'

def convert_salary(val):
    if val < 26 or (val > 50 and val < 66) or val > 70:
        raise ValueError("Salary must be between 26 and 50 inclusive and 66 and 70 inclusive")
    elif val <= 30:
        return '26k..30k'
    elif val <= 35:
        return '31k..35k'
    elif val <= 40:
        return '36k..40k'
    elif val <= 45:
        return '41k..45k'
    elif val <= 50:
        return '46k..50k'
    else:
        return '66k..70k'

df = pd.read_csv('hwk03.csv')

# pipeline => vectorize dict input => Decision Tree classifier
pipe = make_pipeline(DictVectorizer(), DecisionTreeClassifier())

# data from csv used to train model
train_X = df[['department', 'age', 'salary']].to_dict('records')
train_y = df['status']

# fit model to training data
pipe.fit(train_X, train_y)

# get user input for prediction
print('Enter tuple for Decision Tree in this format: DEPARTMENT AGE SALARY')
query_str = input('>> ')
print()

# split input on space and build dict from split
query = query_str.split(' ')
age = convert_age(int(query[1]))
salary = convert_salary(int(query[2].rstrip('k')))
tup_dict = {'department': query[0], 'age': age, 'salary': salary}

# get prediction from user input as dict
pred = pipe.predict(tup_dict)

# print user input and result predicted by model
print('Decision Tree Prediction of {}:'.format(tup_dict))
print(pred[0])

