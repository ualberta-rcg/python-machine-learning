import sklearn
import sklearn.datasets
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import math

# Set a random seed for reproducability
np.random.seed(1337)

# Get/load the data into a dataframe ...
california = sklearn.datasets.fetch_california_housing()
california_df = pd.DataFrame(california['data'], columns=california['feature_names'])
california_df['MedHouseVal'] = california['target']

# Remove outliers ...
income_cut_off = california_df.MedInc.mean() + 3 * california_df.MedInc.std()
california_df = california_df[california_df.MedInc < income_cut_off]

room_cut_off = california_df.AveRooms.mean() + 3 * california_df.AveRooms.std()
california_df = california_df[california_df.AveRooms < room_cut_off]

### My engineered feature ...
### Getting San Fran longitude/latitude from Google
sf_lat = 37.7749
sf_long = -122.4194
d2 = (california_df.Latitude - sf_lat)**2 + (california_df.Longitude - sf_long)**2
california_df['DistSanFran']= d2.apply(math.sqrt)

# Choose features/labels
X = california_df[["MedInc", "AveRooms", "HouseAge", "DistSanFran"]]
y = california_df["MedHouseVal"]

# Split data into training and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

# Select model and train it
model = GradientBoostingRegressor(n_estimators=200)
#model = LinearRegression()
model = model.fit(X_train, y_train)

# Make prediction
predictions = model.predict(X_test)

# Evaluate predictions
print('Mean Absolute Error:', mean_absolute_error(y_test, predictions))
print('Mean Squared Error:', mean_squared_error(y_test, predictions))
print('R2 Score:', r2_score(y_test, predictions))
