from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
dataset = pd.read_csv('../data/final_data.csv')

#clean data - we missed a NaN in our avgBikeDuration...
#print(dataset.isna().sum())
dataset.dropna(subset=['avgBikeDuration'], inplace=True)

# i also had a 17 avg bike durations which was a huge outlier and an error in collection or a day when citibikes were off
# so i remove it

outlier_index = dataset[dataset['avgBikeDuration'] == 17.0].index
dataset.drop(outlier_index, inplace=True)

lst = [('avgTemp', 'avgTaxiDuration')]

for (xstr, ystr) in lst:
    X = dataset[xstr]
    y = dataset[ystr]

    # I decided not to scale it because I wanted it to display the correct values on the graph
    # scaler = StandardScaler()
    # X = scaler.fit_transform(X.values.reshape(-1, 1))

    # Use train_test_split to split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) 

    print("Train set:", X_train.shape, y_train.shape)
    print("Test set:", X_test.shape, y_test.shape)

    # # Convert to df 
    X_train = X_train.to_frame()
    X_test = X_test.to_frame()

    reg = LinearRegression().fit(X_train, y_train) 

    # Print training R-squared
    print('Training R-squared:', reg.score(X_train, y_train))

    # Predict test values
    yhat = reg.predict(X_test) 

    # Print testing R-squared
    testing_r = reg.score(X_test, y_test) 
    print('Testing R-squared:', testing_r)

    # Get the coef and intercept values (y=mx+b)
    m = reg.coef_[0]
    b = reg.intercept_
    print("coef: ", m)
    print("intercept: ", b)

    # Scatter plot
    plt.scatter(X_train, y_train, color= 'orange')
    plt.scatter(X_test, y_test, color = 'green')

    # Regression plot
    x = np.arange(X.min(), X.max())
    plt.plot(x, m*x+b, 'blue')

    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.legend(["Training data", "Testing data", "Regression Line"])
    plt.title(xstr + " vs. " + ystr)

    plt.show()
