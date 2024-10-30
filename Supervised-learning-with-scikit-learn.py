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
# PREPROCESSING DATA- SCIKIT-LEARN ONLY ACCEPTS NUMERIC VALUES
# TO CRETA DUMMY VARIABLES
OneHotEncoder()  # SCIKIT-LEARN
get_dummies()    # PANDAS
# ENCODING DUMMY VARIABLES
import pandas as pd
music_df= pd.read_csv('music.csv')
music_dummies= pd.get_dummies(music_df['genre'], drop_first=True) #genre being the categorical column
# add binary features back to original DF
music_dummies= pd.concat([music_df,music_dummies], axis=1)
music_dummies= music_dummies.drop('genre',axis=1) #remove original genre column
music_dummies= pd.get_dummies(music_df, drop_first=True) #FOR DF with 1 categorical feature
# Linear regression with dummy variables
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression
X= music_dummies.drop('popularity',axis=1).values #contains all features in music_dummies
y= music_dummies['popularity'].values  #contains popularity column
X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2,random_state=42)
kf= KFold(n_splits=5,shuffle=True, random_state=42)
linreg=LinearRegression()
linreg_cv= cross_val_score(linreg, X_train, y_train, cv=kf,scoring='neg_mean_squared_error')
print(np.sqrt(-linreg_cv)  #training RMSE
print("Average RMSE: {}".format(np.mean(rmse)))
print("Standard Deviation of the target array: {}".format(np.std(y)))
# HANDLING MISSING DATA
print(music_df.isna().sum().sort_values()) # to show sum of missing feature values
# DROPPING MISSING DATA- USED WHEN MISSING DATA IS LESS THAN 5% OF ALL DATA
music_df= music_df.dropna(subset=['genre','tempo','loudness']) # Columns with <5% missing values
#IMPUTING VALUES - replace missing data with educated guesses; using mean, median, e.t.c.
#data must be plit first to avoid data leakage
from sklearn.impute import SimpleImputer
X_cat= music_df['genre'].values.reshape(-1,1)
X_num= music_df.drop(['genre','popularity'],axis=1).values
y= music_df['popularity'].values
X_train_cat, X_test_cat, y_train, y_test= train_test_split(X_cat,y, test_size=0.2,random_state=12)                                                           
X_train_num, X_test_num, y_train, y_test= train_test_split(X_num, y, test_size=0.2,random_state=12)                                                   
imp_cat= SimpleImputer(strategy='most_frequent')
X_train_cat= imp_cat.fit_transfrom(X_train_cat)
X_test_cat= imp_cat.transform(X_test_cat)
imp_num= SimpleImputer()   # imputers are knwn as transformers
X_train_num= imp_num.fit_transfrom(X_train_num)
X_test_num= imp_num.transfrom(X_test_num)
X_train= np.append(X_train_num,X_train_cat, axis=1)
X_test= np.append(X_test_num, X_test_cat, axis=1)
#IMPUTING WITHIN A PIPELINE
from sklearn.pipeline import Pipeline
music_df= music_df.dropna(subset=['genre','liveness','tempo'])
music_df['genre']= np.where(music_df['genre']== 'Rock',1,0)
X = music_df.drop('genre',axis=1).values
y= music_df['genre'].values
steps= [('imputation', SimpleImputer()),('logistic_regression',LogisticRegression())]
pipeline= Pipeline(steps)
X-train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.3,random_state=42)
pipeline.fit(X_train,y_train)
pipeline.score(X_test, y_test)
# Build steps for the pipeline
steps = [("imputer", imputer), ("knn", knn)]
# CENTERING AND SCALING DATA - NORMALIZING AND STANDARDIZING DATA
#STANDARDIZATION= subtract mean and divide by variance
#NORMALIZATION= subtract the minimum and divide by the range
#SCALING
from sklearn.preprocessing import StandardScaler
X= music_df.drop('genre',axis=1).values
y= music_df['genre'].values
X_train,X_test,y_train,y_test= train_test_split(X,y,
                                                test_size=0.2,random_state=42)
scaler= StandardScaler()
X_train_scaled= scaler.fit_transform(X_train)
X_test_scaled= scaler.transfrom(X_test)
print(np.mean(X), np.std(X))
print(np.mean(X_train_scaled),np.std(X_train_scaled))
# SCALING IN A PIPELINE
steps= [('scaler', StandardScaler()), ('knn',KNeighborsClassifier(n_neighbors=6))]
pipeline= Pipeline(steps)
X_train,X_test,y_train,y_test= train_test_split(X,y, test_size=0.2,random_state=21)
knn_scaled= pipeline.fit(X_train,y_train)
y_pred= knn_scaled.predict(X_test)
print(knn_scaled.score(X_test,y_test))
# COMPARING PERFORMANCE USING UNSCALED DATA
X_train,X_test,y_train,y_test= train_test_split(X,y, test_size=0.2,random_state=21)
knn_unscaled= KNeighborsClassifier(n_neighbors=6).fit(X_train,y_train)
print(knn_unscaled.score(X_test,y_test))
#CROSS VALIDATION AND SCALING IN A PIPELINE
from sklearn.model_selection import GridSearchCV
steps= [('scaler', StandardScaler()), ('knn',KNeighborsClassifier())]
pipeline= Pipeline(steps)
parameters= {'knn__n_neighbors': np.arange(1,50)}  #specify hyperparameter space by creating DICTIONARY
# Create the parameter space
parameters = {"logreg__C": np.linspace(0.001, 1.0, 20)}
X_train,X_test,y_train,y_test= train_test_split(X,y, test_size=0.2,random_state=21)
cv= GridSearchCV(pipeline,param_grid= parameters)
cv.fit(X_train,y_train)
y_pred= cv.predict(X_test)
print(cv.best_score_)  #check model performance
print(cv.best_params_) # print best parameters, optimal model has result neighbors
# EVALUATING MULTIPLE MODELS
# REGRESSION MODEL PERFORMANCE EVALUATED WITH RMSE & R_SQUARED
#CLASSIFICATION MODEL WITH ACCURACY, CONFUSION-MATRIX,PRECISION-RECALL-F1-SCORE, ROC AUC
# MODELS AFFECTED BY SCALING:KNN, LINREG(+RIDGE,LASSO), LOGREG, ARTIFICIAL NEURAL NETWORK
#EVALUATING CLASSIFICATION MODELS - whic model is better?
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.neighbors import KNeighboursClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
X= music.drop('genre', axis= 1).values
y= music['genre'].values
X_train, X_test,y_train,y_test= train_test_split(X,y,random_state=42)
scaler= StandardScaler()
X_train_scaled= scaler.fit_transform(X_train)
X_test_scaled= scaler.transform(X_test)
models= {'LogReg':LogisticRegression(),
         'KNN':KNeighborsClassifier(),'Decision Tree':DecisionTreeClassifier()}
results= []
for model in models.values():
  kf= KFold(n_splits=6,random_state=42,shuffle=True)
  cv_results= cross_val_score(model,X_train_sclaed,y_train,cv=kf)
  results.append(cv_results)
  plt.boxplot(results,labels=models.keys())
  plt.show()
#Test set performance
for name,model in models.items():
  model.fit(X_train_scaled,y_train)
  test_score= model.score(X_test_scaled,y_test)
  print('{} Test Set Accuracy: {}'.format(name,test_score))
#Test performance using RMSE  
# Import mean_squared_error
from sklearn.metrics import mean_squared_error
for name, model in models.items():
  # Fit the model to the training data
  model.fit(X_train_scaled,y_train)
  # Make predictions on the test set
  y_pred = model.predict(X_test_scaled)
  # Calculate the test_rmse
  test_rmse = mean_squared_error(y_test, y_pred, squared=False)
  print("{} Test Set RMSE: {}".format(name, test_rmse))
#Pipeline for predicting song popularity
# Create steps
steps = [("imp_mean", SimpleImputer()), 
         ("scaler", StandardScaler()), 
         ("logreg", LogisticRegression())]
# Set up pipeline
pipeline = Pipeline(steps)
params = {"logreg__solver": ["newton-cg", "saga", "lbfgs"],
         "logreg__C": np.linspace(0.001, 1.0, 10)}
# Create the GridSearchCV object
tuning = GridSearchCV(pipeline, param_grid=params)
tuning.fit(X_train, y_train)
y_pred = tuning.predict(X_test)
# Compute and print performance
print("Tuned Logistic Regression Parameters: {}, Accuracy: {}".format(tuning.best_params_, t
                                                                      uning.score(X_test,y_test)))





















