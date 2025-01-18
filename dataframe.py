#specify row labels in a table
brics.index = ["infos to add"]
#extracting infos as pandas DF in whole columns in a DF
brics[['column1', 'column2']]
#use slicing to extract rows in DF
brics[1:4] to extract info from the 2nd row to the 4th(n-1)
#pinpoint and extract all data in a row as panda series and panda DF on a DF using loc
brics.loc['RU'] or brics.loc[['RU']]
#for multiple rows
brics.loc[['RU', 'IN', 'CH']]
# extract bool value of all data in a colunm as Series
dr = brics['column number']
#to do the above with one line of code
sel = brics[brics['column no']]

#extracting from beginning to end
brics.loc[:, ['column1', 'column2']]

#extract sub-DF
cars.loc['IN', 'cars_per_cap']
cars.iloc[3, 0]
#or
cars.loc[['IN', 'RU'], 'cars_per_cap']
cars.iloc[[3, 4], 0]
#or
cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
cars.iloc[[3, 4], [0, 1]]

# filtering pandas DF
brics["area"] > 8 #print bool of data in the column area that is larger than 8
# save the above as is_huge, then index it in the main DF to create a subset DF which will contain only values from DF larger than 8
brics[is_huge]
# to get the above done in one line of code
brics[brics['area'] > 8]

# to compare values in a DF
import numpy as np
np.logical_and(brics['area'] > 8, brics['area'] < 10 #to get the bool values
# or
brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)]

#print out label of row and data in row as Panda series in DF
for lab, row in brics.iterrows():
    print(lab)
    print(row)

#print specific row in DF using for loop
for lab, row in brics.iterrows():
    print(lab + ":" + row["capital"])
  
#access column values using the column name as a key in a DF for loop
print(lab + ": " + str(row["column_name"]))

#add column that contains names of country in uppercase using for loop
for lab, row in cars.iterrrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
#most efficient way to do what is above
cars["COUNTRY"] = cars["country"].apply(str.upper)

#add new column for name length in a DF
for lab, row in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row["country"])
print(brics)
#most efficient way to do what is above
brics["name_length"] = brics["country"].apply(len)
print(brics)

#extract data of ages more than 25 in a DF
high_above_25 = df[df['Age'] > 25]
#subsetting rows
dogs[dogs['height_cm'] > 50]
#calculate mean for a colum in a DF
games_home['PLUS_MINUS'].mean()

#applying transform to a DF
df = df.transform(func = lambda x : x + 10)
print(df)
#find sqt of each element in the DF
result = df.transform(func = ['sqrt]')

#sort 1 column(smallest to largest)
df.sort_values('column_name', ascending= False)
#sort multiple columns
df.sort_values(['column_name1', 'column_name2'])
#EG of sort multiple colums
home_fam = house.sort_values(['region','family'], ascending=[True,False])
#select multiple columns of a DF
df[['col_a', 'col_b']]

#filtering or selecting rows under multiple conditions [for and or condition use "|"]
dogs[(dogs['height_cm'] > 60) & (dogs['color'] == 'tan')]
#subsettin rows by categorical variables using .isin() method. homelessness is the DF
canu = ["California", "Arizona", "Nevada", "Utah"]
mojave_homelessness = homelessness["state"].isin(canu)
homelessness[mojave_homelessness]
print(mojave_homelessness)

#create new column in DF
df['new_column'] = df['existing_column'] / 100
# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita']= gdp_pop['gdp'] / gdp_pop['pop']

# EXAMPLE: Which state has the highest number of homeless individuals per 10,000 people in the state?
# Create indiv_per_10k col as homeless individuals per 10k state pop   EG
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 
# Subset rows for indiv_per_10k greater than 20   EG
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]
# Sort high_homelessness by descending indiv_per_10k   EG
high_homelessness_srt = high_homelessness.sort_values(["indiv_per_10k"], ascending= False)
# From high_homelessness_srt, select the state and indiv_per_10k cols   EG
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# To get cummulative sum
dogs['weight_kg'].cumsum()
# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()
# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()
# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)
#mean, median, min, max of column in a DF
print(sales["weekly_sales"].mean())

#drop duplicate names (name is the column we want to check for duplicates)
vet_visits.drop_duplicates(subset='name')
#drop duplicate pairs
unique_dogs = vet_visits.drop_duplicates(subset= ['name', 'breed'])
# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

#sort and count values
unique_dogs['breed'].value_counts(sort=True)
#proportions  (get percentage of values)
unique_dogs['breed'].value_counts(normalize=True)
# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

#Grouped summaries   (group by color variable and slect the weight column along with getting mean)
dogs.groupby('color')['weight_kg'].mean()
#Multiple grouped summaries
dogs.groupby('color')['weight_kg'].agg([min, max, sum])
#Grouping by multiple variables
dogs.groupby(['color', 'breed'])['weight_kg'].mean()
#Group many groups, many summaries
dogs.groupby(['color', 'breed'])[['weight_kg', 'height_cm']].mean()
# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([min, max, np.mean, np.median])
# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

#Group by to pivot table
dogs.pivot_table(values='weight_kg', index='color')
#Multiple statistics with pivot table
dogs.pivot_table(values='weight_kg', index='color', aggfunc=[np.mean, np.median])
#Pivot on two variables
dogs.pivot_table(values='weight_kg', index='color', columns='breed')
#filling missing values in pivot tables
dogs.pivot_table(values='weight_kg', index='color', columns='breed', fill_value=0)
#summing to get mean of column and row in pivot tables
dogs.pivot_table(values='weight_kg', index='color', columns='breed', fill_value=0, margins=True)
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")
# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])
# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))
# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index=["country","city"], columns="year")

#Setting a column as index
dogs_ind= dogs.set_index('name')
#Remove an index
dogs_ind.reset_index()
#Dropping an index
dogs_ind.reset_index(drop=True)
#Multi-level indexes-hierarchical indexes
dogs_ind3 = dogs.set_index(['breed', 'color'])
#sorting by index values
dogs_ind3.sort_index()
#Controlling sort_index
dogs_ind3.sort_index(level=['color', 'breed'], ascending= [True, False])
# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))
# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending= [True, False]))
# Sort index in DF before slicing
dogs_srt = dogs.set_index(['breed', 'color']).sort_index()

#Subsetting with indexes
dogs[dogs['name'].isin(['Bella', 'stella'])]
#Subsetting with Loc- filters on index values
dogs_ind.loc[['Bella', 'Stella']]
#subsetting on duplicated index values
dogs_ind2.loc['Labrador']
#subset outer level with a list
dogs_ind3.loc[['Labrador', 'Chihuahua']]
#subset inner levels with a list of tuples
dogs_ind3.loc[[('Labra', 'Brown'), ('chihua', 'Tan')]]
#Subset avocados for the conventional type price column. Create a histogram.
avocados[avocados["type"]==["conventional"]["avg_price"]].hist()

#Slicing outer index level
dogs_srt.loc['chow': 'poodle']
#Slicing inner index levels
dogs_srt.loc[('Labrador', 'Brown'): ('Schnauzer', 'Grey')]
#Slicing columns
dogs_srt.loc[:, 'name':'height_cm']
#Slice rows and columns
dogs_srt.loc[('Lab', 'Brown'):('Sch', 'Grey'), 'name':'height_cm']
#slicing dates
dogs.loc['2014-08-25':'2016-09-16'] or dogs.loc['2014':'2016']

#Subsetting by row/column number
dogs.iloc[2:5,1:4]
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"]<= "2011-01-01")]
# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])
# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])
# Use slicing in both directions at once
print(temperatures.iloc[:5,2:4])

#Axis argument :index means- calculate the stats across rows
dogs_height.mean(axis="index")
#Axis argument for across columns
dogs_height.mean(axis="columns")

#Access the components of a date (year, month and day)
temperatures["year"] = temperatures["date"].dt.year

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()
# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])
# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")
# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])

#Detecting missing values
dogs.isna()
#Detecting any missing values
dog.isna().any()
#Counting missing values
dogs.isna().sum()
#Plotting missing values
dogs.isna().sum().plot(kind='bar')
plt.show()
#Removing missing values
dogs.dropna()
#Replacing missing values(best if you are working with large data)
dogs.fillna(0)






























               
