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

























