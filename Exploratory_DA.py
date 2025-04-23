import pandas as pd
# GATHER MORE INFO
books.info()
# CHECK DATA TYPES
books.dtypes
# LOOK A CAEGORICAL COLUMNS
books.value_counts('genre')
# DESCRIBE NUMERICAL COLUMNS
books.describe()
# VISUALIZING NUM DATA
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(data=books, x='rating')
plt.show()
# ADJUSTING BIN WIDTH
sns.histplot(data=books, x='rating', binwidth=.1)

# EXERCISE 1
# Import the required visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt
# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(data=unemployment,x='2021',binwidth=1)
plt.show()

# DATA VALIDATION
#Updating datatypes- to int
books['year']= books['year'].astype(int)
# VALIDATING CAT. DATA
books['genre'].isin(['fiction', 'non fiction'])
~books['genre'].isin(['fiction', 'non fiction']) # to invert result of the above

# VALIDATING NUM DATA - to view only numerical columns
books.select_dtypes('number').head()
books['year'].min()   # get minimum
books['year'].max()   # get maximum
sns.boxplot(data=books,x='year',y='genre') # view year data by cat. variable
# EXERCISE 1
# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment['continent'].isin(['Oceania'])
# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])

# Print the minimum and maximum unemployment rates during 2021
print(unemployment['2021'].min(), unemployment['2021'].max())

# Create a boxplot of 2021 unemployment rates, broken down by continent
sns.boxplot(data=unemployment,x='2021',y='continent')
plt.show()

# DATA SUMMARIZATION
# EXPLORING GROUPS OF DATA
# .groupby() groups data by cat
books.groupby('genre').mean()
books.agg(['mean','std'])
# Print yearly mean and standard deviation grouped by continent
print(unemployment.groupby('continent').agg(['mean','std']))
# SPECIFY AGGREGATION FOR COLUMNS
books.agg({'rating':['mean','std'],'year':['median']})
# NAMED SUMMARY COLUMNS
books.groupby('genre').agg(mean_rating=('rating','mean'),std_rat=('rating','std'),
                           median_year=('year','median'))
# EXAMPLE OF CODE ABOVE
continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021=('2021','mean'),
    # Create the std_rate_2021 column
    std_rate_2021=('2021','std')
)
print(continent_summary)

# VISUALIZING CAT SUMMARIES
sns.barplot(data=books,x='genre',y='rating')
plt.show()

# ADDRESSING MISSING DATA
# COUNT MISSING VALUES - columns with missing values
print(salaries.isna().sum())
# Strategies that could be used
# 1. Drop missing values if it's 5% or less of total values
# 2. Impute mean, median, mode depending on distribution and context
# 3. Impute by sub-group- diff eperience levels have diff median salary

# DROPPING MISSING VALUES 
# MISSING VALUES THERSHOLD
threshold= len(salaries)* 0.05
print(threshold)
#create filter
cols_to_drop= salaries.columns[salaries.isna().sum()<=threshold]
# drop missing val for col below threshold
salaries.dropna(subset=cols_to_drop, inplace=True)
# IMPUTING SUMMARY STATS
cols_with_missing_values= salaries.columns[salaries.isna().sum() >0]
print(cols_with_missing_values)
for col in cols_with_missing_values[:-1]:
  salaries[col].fillna(salaries[col].mode()[0])
# IMPUTING BY SUB-GROUP- returns median salary for each experience level
salaries_dict= salaries.groupby('Experience')['Salary_usd'].median().to_dict()
print(salaries_dict)
salaries['Salary_usd'] = salaries['Salary_usd'].fillna(salaries['Experience'].map(salaries_dict))
# when missing values are checked again there will be no missing values

# EXERCISE 1














