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
X = diabetes_df.drop('glucose', axis=1).values  #or  X = sales_df['radio'].values
y = diabetes_df['glucose'].values
# Makke predictions from a single feature - array must be 2D to be accepted by scikit-learn
X_bmi = X[:,3]
X_bmi = X_bmi.reshape(-1,1)   # convert shape
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
print("Predictions: {}, Actual Values: {}".format(y_pred[:2], y_test[:2]))
plt.scatter(X_bmi, y)
plt.plot(X_bmi, predictions)
plt.ylabel('Blood Glucose (mg/dl)')
plt.xlabel('Body Mass Index')
plt.show()
# Linear regression using all features
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test= train_test_split(X,
                                                   y, test_size=0.3,
                                                   random_state=42)
reg_all = LiinearRegression()
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test)
# Computing R-squared - default metric for L.Regression
reg_all.score(X_test,y_test)
# RMSE (ROOT MEAN SQUARED ERROR - CONVERT TO DOLLARS squared = True?
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred, squared=False)
# Import mean_squared_error
from sklearn.metrics import mean_squared_error
# Compute R-squared
r_squared = reg.score(X_test, y_test) # score = ridge.score(X_test,y_test)
# Compute RMSE
rmse = mean_squared_error(y_test, y_pred, squared=False)
# Print the metrics
print("R^2: {}".format(r_squared))
print("RMSE: {}".format(rmse))
# CROSS-VALIDATION FOR MODEL PERFORMANCE
from sklearn.model_selection import cross_val_score, KFold
kf= KFold(n_splits=6, shuffle=True, random_state=42)
reg= LinearRegression()
cv_results= cross_val_score(reg, X, y, cv=kf)
print(cv_results)
print(np.quantile(cv_results,[0.025,0.975]))   # 95% confidence interval- upper and lower limits of interval
# REGULARIZED REGRESSION - AVOIDS OVERFITTING
# RIDGE REGRESSION
from sklearn.linear_model import Ridge
scores= []
for alpha in [0.1,1.0,10.0,100.0,1000.0]:
  ridge= Ridge(alpha=alpha)
  ridge.fit(X_train, y_train)
  y_pred=ridge.predict(X_test)
  scores.append(ridge.score(X_test,y_test))
print(scores)
# LASSO REGRESSION - for feature selection
from sklearn.linear_model import Lasso
scores = []
for alpha in [0.01,1.0,10.0,20.0,50.0]:
  lasso = Lasso(alpha=alpha)
  lasso.fit(X_train, y_train)
  lasso_pred= lasso.predict(X_test)
  scores.append(lass0.score(X_test, y_test))
print(scores)
# LASSO REGRESSION for feature selection
from sklearn.linear_model import Lasso
X = diabetes_df.drop('glucose', axis=1).values
y = diabetes_df['glucose'].values
names = diabetes_df.drop('glucose', axis=1).columns
lasso= Lasso(alpha=0.1)
lasso_coef= Lasso(alpha=0.1)
lasso_coef= lasso.fit(X,y).coef_  #fit model to data and extract coefficients
plt.bar(names, lasso_coef)    # plot coefficients for each feature
plt.xticks(rotation=45)
plt.show()
# Confusion matrix in scikit-learn
from sklearn.metrics import classification_report, confusion_matrix
knn= KNeighborsClassifier(n_neighbors=7)
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.4, random_state=42)
knn.fit(X_train, y_train)
y_pred=knn.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))   # gives a classification report on metrics
# LOGISTIC REGRESSION - this often perfroms better than KNN model across metrics
from sklearn.linear_model import LogisticRegression
logreg= LogisticRegression()
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.3, random_state=42)
logreg.fit(X_train, y_train)
y_pred= logreg.predict(X_test)
y_pred_probs = logreg.predict_proba(X_test)[:,1]  #predicting probabilities
print(y_pred_probs[0])
# PLOTTING ROC curve - model performs better when ROC curve is above dotted line
from sklearn.metrics import roc_curve
fpr, tpr, thresholds= roc_curve(y_test, y_pred_probs)
plt.plot([0,1],[0,1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
pt.title('Logistic Regression ROC Curve')
plt.show()
# ROC AUC - Area Under ROC Curve 
from sklearn.metrics import roc_auc_score
print(roc_auc_score(y_test, y_pred_probs))
# HYPERPARAMETER TUNING - PARAMETERS SPECIFIED BEFORE FITTING THE MODEL(ALPHS OR N_NEIGHBORS)
# GRIDSEARCHCV IN SCIKIT-LEARN
from sklearn.model_selection import GridSearchCV
kf= KFold(n_splits=5, shuffle= True, random_state=42)
param_grid= {'alpha': np.arrange(0.0001,1,10),'solver':['sag','lsqr']}
ridge= Ridge()
ridge_cv= GridSearchCV(ridge, param_grid, cv=kf)
ridge_cv.fit(X_train, y_train)
print(ridge_cv.best_params_, ridge_cv.best_score_)
# RandomizedSearchCV
from sklearn.model_selection import RandomizedSearchCV
kf= KFold(n_splits=5, shuffle= True, random_state=42)
param_grid= {'alpha': np.arrange(0.0001,1,10),'solver':['sag','lsqr']}
ridge= Ridge()
ridge_cv= RandomizedSearchCV(ridge, param_grid, cv=kf, n_iter=2)
ridge_cv.fit(X_train, y_train)
print(ridge_cv.best_params_, ridge_cv.best_score_)
test_score= ridge_cv.score(X_test, y_test)  # Evaluate on test set
print(test_score)
# Create the parameter space
params = {"penalty": ["l1", "l2"],
         "tol": np.linspace(0.0001, 1.0, 50),
         "C": np.linspace(0.1, 1.0, 50),
         "class_weight": ["balanced", {0:0.8, 1:0.2}]}
logreg_cv = RandomizedSearchCV(logreg, params, cv=kf)  # Instantiate the RandomizedSearchCV object
logreg_cv.fit(X_train, y_train)    # Fit the data to the model
# Print the tuned parameters and score
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
print("Tuned Logistic Regression Best Accuracy Score: {}".format(logreg_cv.best_score_))































