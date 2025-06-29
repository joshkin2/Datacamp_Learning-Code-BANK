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
# Count the number of missing values in each column
print(planes.isna().sum())
# Find the five percent threshold
threshold = len(planes) * 0.05
# Create a filter
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]
# Drop missing values for columns below the threshold
planes.dropna(subset=cols_to_drop, inplace=True)
print(planes.isna().sum())
# Check the values of the Additional_Info column
print(planes["Additional_Info"].value_counts())
# Create a box plot of Price by Airline
sns.boxplot(data=planes, x='Airline', y='Price')
plt.show()
# remove add_info colum and impute median by airline for missing price values
# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()
print(airline_prices)
# Convert to a dictionary
prices_dict = airline_prices.to_dict()
# Map the dictionary to missing values of Price by Airline
planes["Price"] = planes["Price"].fillna(planes["Airline"].map(prices_dict))
# Check for missing values
print(planes.isna().sum())

#CONVERTING AND ANALYZING CAT DATA
# PREVIEWING THE DATA
print(salaries.select_dtypes('object').head())
# JOB TITLES
print(salaries['Designation'].value_counts())
# COUNT UNIQUE JOB TITLES
print(salaries['Designtation'].nunique())
# EXTRACTING VALUE FROM CAT
pandas.Series.str.contains()
# SEARCH COLUMN FOR SPECIFIC STR OR MULTIPLE STR
salaries['Designation'].str.contains('Scientist')
# FIND MULTIPLE PHRASES IN STRS
salaries['Designation'].str.contains('Machine Learning|AI')
# FIND MULTIPLE PHRASES IN STRS THAT START WITH A WORD
salaries['Designation'].str.contains('^Data')

conditions=[(salaries['Designation'].str.contains('Scientist')),
            (salaries['Designation'].str.contains('Scientist'))]
#CREATE CAT COLUMN
salaries['Job_Category']= np.select(conditions,job_categories,default='Other')
# VISUALIZE JOB CAT FREQUENCY
sns.countplot(data=salaries, x='Job_Category')
plt.show()

#EXERCISE 
# Finding the number of unique values
# Filter the DataFrame for object columns
non_numeric = planes.select_dtypes("object")
# Loop through columns
for plane in non_numeric.columns:  
  # Print the number of unique values
  print(f"Number of unique values in {plane} column: ", non_numeric[plane].nunique())
# Create a list of categories
flight_categories = ["Short-haul", "Medium", "Long-haul"]
# Create short_flights
short_flights = "^0h|^1h|^2h|^3h|^4h"
# Create medium_flights
medium_flights = "^5h|^6h|^7h|^8h|^9h"
# Create long_flights
long_flights = "10h|11h|12h|13h|14h|15h|16h"
# Create conditions for values in flight_categories to be created
conditions = [
    (planes["Duration"].str.contains(short_flights)),
    (planes["Duration"].str.contains(medium_flights)),
    (planes["Duration"].str.contains(long_flights))
]
# Apply the conditions list to the flight_categories
planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration")
# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")
plt.show()

# WORKING WITH NUMERIC DATA
#CONVERT STRINGS TO NUMBERS
# 1ST REMOVE COMMA VALUES
salaries['Salary_in_rupees']= salaries['Salary_in_rupees'].str.replace(',','')
# 2ND CHANGE COLUMN TO FLOAT
salaries['Salary_in_rupees']= salaries['Salary_in_rupees'].astype(float)
# 3RD CREATE NEW COLUMN BY CONVERTING CURRENCY
salaries['Salary_in_usd']=salaries['Salary_in_rupees'] * 0.012
# ADD SUMMARY STATS INTO DF
salaries['std_dev']= salaries.groupby('Experience')['Salary_usd'].transform(lambda x:x.std())
print(salaries[['Experience','std_dev']].value_counts())
salaries['median_by_comp_size']= salaries.groupby('Company_size')\['Salary_usd'].transform(lambda x:x.median())

# EXERCISE
# Preview the column
print(planes["Duration"].head())
# Remove the string character
planes["Duration"] = planes["Duration"].str.replace("h", "")
# Convert to float data type
planes["Duration"] = planes["Duration"].astype(float)
# Plot a histogram
sns.histplot(data=planes,x="Duration")
plt.show()
# ADD DESCRIPTIVE STATS TO THE ABOVE EXERCISE
# Price standard deviation by Airline
planes["airline_price_st_dev"] = planes.groupby("Airline")["Price"].transform(lambda x: x.std())
print(planes[["Airline", "airline_price_st_dev"]].value_counts())
# Median Duration by Airline
planes["airline_median_duration"] = planes.groupby("Airline")["Price"].transform(lambda x: x.median())
print(planes[["Airline","airline_median_duration"]].value_counts())
# Mean Price by Destination
planes["price_destination_mean"] = planes.groupby("Destination")["Price"].transform(lambda x: x.mean())
print(planes[["Destination","price_destination_mean"]].value_counts())

# HANDLING OUTLIERS
# IDENTIFY OUTLIER BY COMPARING MAX TO MEAN VALUE
print(salaries['Salary_usd'].describe())
# FIND OUTLIERS USING IQR
sns.boxplot(data=salaries,y='salary_usd')
plt.show()   # we can get the 75th&25th percentile from graph
# UPPER OUTLIERS= VALIES ABOVE 75TH + (1.5*IQR)
# LOWER= VALUES BELOW 25TH - (1.5*iqr)
# CALCULATING PERCENTILES and identifying outliers with quantile()
seventy_fifth= salaries['salary_usd'].quantile(0.75)
twenty_fifth= salaries['salary_usd'].quantile(0.25)
salaries_iqr= seventy_fifth - twenty_fifth
upper= seventy_fifth+(1.5 * salaries_iqr)
lower=twenty_fifth-(1.5*salaries_iqr)
print(upper,lower)
# SUBSETTING DATA
salaries[(salaries['salary_usd'] < lower) | (salaries['salary_usd'] > upper)][['Experience', 'employee_location', 'salary_usd']]
# WE LOOK FOR OUTLIERS BECAUSE STATS TESTS AND ML MODELS NEED NORMALLY DISTRIBUTED DATA
# DROPPING OUTLIERS
no_outliers= salaries[(salaries['salary_usd']>lower) & (salaries['salary_usd']<
                                           upper)]
print(no_outliers['salary_usd'].describe())

#EXECISE
# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)
# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth
# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)
# Subset the data
planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]
print(planes["Price"].describe())

# PATTERNS OVERTIME
divorce = pd.read_csv("divorce.csv")
# IMPORTING DATETIME DATA
divorce=pd.read_csv("divorce.csv", parse_date=["marriage_date"])
# CONVERTING TO DATETIME DATA
divorce["marriage_data"]= pd.to_datetime(divorce["marriage_date"])
# CONVERT 3 DATE COLUMNS (MNTH. DAY, YEAR) TO 1 COLUMN
divorce["marriage_date"]= pd.to_datetime(divorce[["month","day","year"]])
# EXTRACT PARTS OF A FULL DATE
divorce["marriage_month"]= divorce["marriage_date"].dt.month
# Define the marriage_year column
divorce["marriage_year"] = divorce["marriage_date"].dt.year

# VISUALIZING PATTERNS OVER TIME
sns.lineplot(data=divorce, x="mariage_month",y="marriage_duration")
plt.show()

# EXERCISE 1
# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv("divorce.csv",parse_dates=["divorce_date","dob_man","dob_woman","marriage_date"])
print(divorce.dtypes)
# Define the marriage_year column
divorce["marriage_year"] = divorce["marriage_date"].dt.year
# Create a line plot showing the average number of kids by year
sns.lineplot(data=divorce,x="marriage_year",y="num_kids")
plt.show()

#CORRELATION
divorce.corr() #pearson corr coefficient - linear only
# CORRELATION HEATMAP
sns.heatmap(divorce.corr(), annot=True)
plt.show()
# SCATTER PLOTS
sns.scatterplot(data=divorce,x="income_man",y= "income_woman")
plt.show()
# PAIRPLOTS
sns.paiplot(data=divorce)
plt.show()
# MINIMIZE PLOTS SHOWN
sns.pairplot(data=divorce,vars=["income_man","income_woman"])
plt.show()

#FACTOR RELATIONSHIPS & DISTRIBUTIONS
#explore categorical relationships
sns.histplot(data=divorce,x="marriage_duration",hue="education_man", binwidth=1)
plt.show()
# FOR CLEARER VISUALIZATION OF ABOVE KDE PLOTS
sns.kdeplot(data=divorce,x="marriage_duration",hue="education_man", cut=0)
plt.show()
CUMULATIVE KDE PLOTS
sns.kdeplot(data=divorce,x="marriage_duration",hue="education_man",cut=0,cumulative=True)
plt.show()

#CHECKING RELATIONSHIP BTW MARRIAGE AGE AND EDUCATIOM
divorce["man_age_marriage"]= divorce["marriage_year"] - divorce["dob_man"].dt.year
divorce["woman_age_marriage"]= divorce["marriage_year"] - divorce["dob_woman"].dt.year
sns.scatterplot(data=divorce, x="woman_age_marriage",y="man_age_marriage",hue="education_man")
plt.show()

# CONSIDERATIONS 4 CAT DATA
# RELATIVE CLASS FREQUENCY
planes["Destination"].value_counts(normalize=True)
#CROSS-TABULATION
pd.crosstab(planes["Source"], planes["Destination"])
# AGG values with pd.crosstab()
pd.crosstab(planes["Source"],planes["Destination"],
            values=planes["Price"], aggfunc="median")

#GENERATING NEW FEATURES
#CLEANING TOTAL STOPS
planes["Total_stops"]= planes["Total_stops"].str.replace(" stops", "")
planes["Total_stops"]= planes["Total_stops"].str.replace(" stop", "")
planes["Total_stops"]= planes["Total_stops"].str.replace("non_stop", "0")
planes["Total_stops"]= planes["Total_stops"].astype(int)
#correlation
sns.heatmap(planes.corr(), annot=True)
plt.show()
# EXTRACTING MONTH AND WEEKDAY
planes["month"]= planes["Date_of_journey"].dt.month
planes["weekday"]= planes["Date_of_journey"].dt.weekday
print(planes[["month","weekday","Date_of_journey"]].head())
# CREATING CATEGORIES using descriptive stats
twenty_fifth= planes["Price"].quantile(0.25)
median=planes["Price"].median()
seventy_fifth= planes["Price"].quantile(0.75)
maximum= planes["Price"].max()
# Labels and bins
labels=["Economy","Premium Eco", "Business Cl", "First Cl"]
bins=[0, twenty_fifth, median, seventy_fifth, maximum]
planes["Price_category"]= pd.cut(planes["Price"],
                                 labels=labels,bins=bins)
print(planes[["Price","Price_category"]].head())
#PRICE CAT BY AIRLINE
sns.countplot(data=planes,x="Airline",hue="Price_category")
plt.show()

#EXERCISE 1
# Create salary labels
salary_labels = ["entry", "mid", "senior", "exec"]
# Create the salary ranges list
salary_ranges = [0, twenty_fifth, salaries_median, seventy_fifth, salaries["Salary_USD"].max()]
# Create salary_level
salaries["salary_level"] = pd.cut(salaries["Salary_USD"],
                                  bins=salary_ranges,
                                  labels=salary_labels)
# Plot the count of salary levels at companies of different sizes
sns.countplot(data=salaries, x="Company_Size", hue="salary_level")
plt.show()

# GENERATING HYPOTHESIS
# SPURIOUS CORRELATION
sns.scatterplot(data=planes, x="duration",y="price",hue="total_stops")
plt.show()
sns.barplot(data=planes, x="airline", y="duration")
plt.show()

#Exercise 1
# Filter for employees in the US or GB
usa_and_gb = salaries[salaries["Employee_Location"].isin(["US", "GB"])]
# Create a barplot of salaries by location
sns.barplot(data=usa_and_gb, x="Employee_Location", y="Salary_USD")
plt.show()
# Create a bar plot of salary versus company size, factoring in employment status
sns.barplot(data=salaries, x="Company_Size", y="Salary_USD", hue="Employment_Status")
plt.show()

