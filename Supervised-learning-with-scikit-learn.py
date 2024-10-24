#feature = predictor var. = independent var.
#target var. = dependent var. = response var
# K-NEAREST NEIGHBORS MODEL USES DISTANCE BTW OBSERVATIONS TO PREDICT LABLES OR VALUES
# SUpervised learning workflow
from sklearn.module import Model
model = Model()
mode.fit(X, y)
# KNN model using scikit-learn
from sklearn.neighbors import KNeighborsClassifier
X = churn_df[['total_day_charge', 'total_eve_charge']].values
Y = churn_df[['churn']].values
knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X, Y)                 #  fitting classifier on labeled data
X_new = np.array([[9,9],      # predicitng on unlabeled data
                  [9,9],
                  [9,9]])
predictions = knn.predict(X_new)
print('Predicitions: {}'.format(predictions))
# MEASURING MODEL PERFORMANCE
# accuracy = correct pred./ total observations
# train/test split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y test_size=0.3,
                                                    random_state=21, stratify=y)
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, Y_train)
print(knn.score(X_test,Y_test)   #check accuracy
# MODEL COMPLEXITY AND OVER/UNDERFITTING
train_accuracies= {}
test_accuracies = {}
neighbors= np.arange(1,26)
for neighbor in neighbors:
  knn = KNeighborsClassifier(n_neighbors=neighbor)
  knn.fit(X_train, Y_train)
  train_accuracies[neighbor]= knn.score(X_train, Y_train)
  test_accuracies[neighbor]= knn.score(X_test, Y_test)
plt.figure(figsize=(8,6))    # plot results
plt.title('KNN: Varying Number of Neighbors')
plt.plot(neighbors, train_accuracies.values(), label='Training Accuracy')
plt.plot(neighbors, test_accuracies.values(), label='Testing Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()
# REGRESSION
# Creating feature and target arrays
X = diabetes_df.drop('glucos', axis=1).values
y = diabetes_df['glucose'].values
# Makke predictions from a single feature - array must be 2D to be accepted by scikit-learn
X_bmi = X[:,3]
X_bmi = X_bmi.reshape(-1,1)   # convert shape)
# plot glucose Vs BMI
import matplotlib.pyplot as plt
plt.scatter(X_bmi, y)
plt.ylabel('Blood Glucose (mg/dl)')
plt.xlabel('Body Mass Index')
plt.show()
# Fitting regression model'
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_bmi, y)
predictions = reg.predict(X_bmi)
plt.scatter(X_bmi, y)
plt.plot(X_bmi, predictions)
plt.ylabel('Blood Glucose (mg/dl)')
plt.xlabel('Body Mass Index')
plt.show()














