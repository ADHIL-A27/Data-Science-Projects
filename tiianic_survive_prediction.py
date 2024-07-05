# -*- coding: utf-8 -*-
"""titanic_survive_prediction.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18rn3DWGiFSbcN5cL94SIqGT0DikIDSU4
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic_data = pd.read_csv("/content/train.csv")

titanic_data.head()

titanic_data.shape

titanic_data.info()

titanic_data.isnull().sum()

titanic_data = titanic_data.drop(columns='Cabin',axis=1)

titanic_data['Age'].fillna(titanic_data['Age'].mean(),inplace=True)

print(titanic_data['Embarked'].mode())

print(titanic_data['Embarked'].mode()[0])

titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0],inplace=True)

titanic_data.isnull().sum()

titanic_data.describe()

titanic_data['Survived'].value_counts()

sns.set()

sns.countplot(x='Survived', data=titanic_data)
plt.show()

titanic_data['Sex'].value_counts()

sns.countplot(x='Sex',data=titanic_data)

# number of survivors Gender wise
sns.countplot(x='Sex', hue='Survived', data=titanic_data)
plt.show()

sns.countplot(x='Pclass',data=titanic_data)

sns.countplot(x='Pclass',hue='Survived',data=titanic_data)

titanic_data['Embarked'].value_counts(

)

titanic_data.replace({"Sex":{'male':0,'female':1},'Embarked':{'S':0,'C':1,'Q':2}},inplace=True)

titanic_data.head()

X = titanic_data.drop(columns = ['PassengerId','Name','Ticket','Survived'],axis=1)
Y = titanic_data['Survived']

print(X)

print(Y)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

model = LogisticRegression()

model.fit(X_train,Y_train)

X_train_prediction = model.predict(X_train)

print(X_train_prediction)

training_data_accuracy = accuracy_score(Y_train,X_train_prediction)
print('Accuracy score of training data: ',training_data_accuracy)

X_test_prediction = model.predict(X_test)

test_data_accuracy = accuracy_score(Y_test,X_test_prediction)
print("Accuracy score of test data: ", test_data_accuracy)

# Load the test data
test_data = pd.read_csv("/content/test.csv")

# Preprocess the test data (same steps as training data)
test_data = test_data.drop(columns='Cabin', axis=1)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].mode()[0], inplace=True)

# Replace categorical values with numerical values
test_data.replace({"Sex":{'male':0,'female':1},'Embarked':{'S':0,'C':1,'Q':2}}, inplace=True)

# Drop unnecessary columns
X_test_data = test_data.drop(columns=['PassengerId', 'Name', 'Ticket'], axis=1)

# Load test data
test_data = pd.read_csv("/content/test.csv")

# Data preprocessing for test data
test_data = test_data.drop(columns='Cabin', axis=1)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].mode()[0], inplace=True)
test_data.replace({"Sex":{'male':0,'female':1},'Embarked':{'S':0,'C':1,'Q':2}}, inplace=True)

# Prepare feature variables for test data
X_test_data = test_data.drop(columns=['PassengerId', 'Name', 'Ticket'], axis=1)

# Verify there are no missing values left
print(test_data.isnull().sum())

# Make predictions on the test data
test_predictions = model.predict(X_test_data)

# Prepare the submission file
submission = pd.DataFrame({
    'PassengerId': test_data['PassengerId'],
    'Survived': test_predictions
})

# Prepare the submission file
submission = pd.DataFrame({
    'PassengerId': test_data['PassengerId'],
    'Survived': test_predictions
})

# Save the submission file
submission.to_csv('submission.csv', index=False)

# Download the submission file (if running in Colab)
from google.colab import files
files.download('submission.csv')

