from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from warnings import simplefilter

import pandas as pd
import matplotlib.pyplot as plt

# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# K-Nearest Neighbor: 
# Given average bike ride time, distance, and bike trips on a given day, predict the weatherDescription
# load all the data & then grab only necessary columns
allData = pd.read_csv("../data/final_data.csv")
allData.dropna(subset=['avgBikeDuration'], inplace=True) # Missed a NaN value during our data cleaning
x = allData[['avgBikeDuration', 'avgBikeDistance', 'totalBikeTrips']]
y = allData['weatherDescription']

# perform one-hot encoding on categorical labels 
OH_encoder = OneHotEncoder()
output = OH_encoder.fit_transform(y.values.reshape(-1, 1)).toarray()

# peform minmax scaling 
scaler = MinMaxScaler() 
norm = scaler.fit_transform(x)
x = pd.DataFrame(norm, columns=x.columns)

x_train, x_val_test, y_train, y_val_test = train_test_split(x, y, test_size= 0.4, random_state= 1)
x_val, x_test, y_val, y_test = train_test_split(x_val_test, y_val_test, test_size= 0.5, random_state= 1) 

# Finding the ideal K
k_vals = range(1,11)
train_accs = []
val_accs = []

for k in k_vals:
    classifier = KNeighborsClassifier(k).fit(x_train, y_train) 
    # predict validation set 
    y_hat = classifier.predict(x_val)
    train_accs.append(metrics.accuracy_score(y_train, classifier.predict(x_train)))
    val_accs.append(metrics.accuracy_score(y_val, y_hat))

plt.plot(k_vals, train_accs, 'b', k_vals, val_accs, 'g')
plt.ylabel("Accuracy")
plt.xlabel("Number of neighbors (k)")
plt.legend(['Training','Validation'])
plt.show()

k = 7

# train model
classifier = KNeighborsClassifier(k).fit(x_train, y_train)

# predict test set
y_hat = classifier.predict(x_test)

train_accuracy = metrics.accuracy_score(y_train, classifier.predict(x_train))
test_accuracy = metrics.accuracy_score(y_test, y_hat)
print("Train set Accuracy: ", train_accuracy)
print("Test set Accuracy: ", test_accuracy)
