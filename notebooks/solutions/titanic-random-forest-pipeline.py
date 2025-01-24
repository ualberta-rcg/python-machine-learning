import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

np.random.seed(1337)

# Load data
train_df = pd.read_csv('data/titanic/train.csv')

# Choose features and lables
features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_df[features], dtype='int64', drop_first=True)
y = train_df['Survived']

# Split data into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

# Initialize model and fit to training data
model = RandomForestClassifier(n_estimators=100, max_depth=3)
model = model.fit(X_train, y_train)

# Use model to predict on unseen test data
predictions = model.predict(X_test)

# Evaluate how well the model did
print('Accuracy: {}'.format(accuracy_score(y_test, predictions)))
print('Precision: {}'.format(precision_score(y_test, predictions)))
print('Recall: {}'.format(recall_score(y_test, predictions)))
