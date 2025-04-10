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

















