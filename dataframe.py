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

# STATISTICS IN PYTHON - MEAN- Average
np.mean(df['column'])
# MEDIAN- BEST USED WHEN DATA IS SKEWED
np.median(df['column'])
# MODE
import statistics
statistics.mode(df['column'])
# OR MODE - CATEGORICAL VALUES
df['column'].value_counts()
#calculate mean for a colum in a DF
games_home['PLUS_MINUS'].mean()
# calculate mean and median of a column in a sales dataset
sales['unit_price'].agg([np.mean, np.median])

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
# Select the title_org, title_seq, and diff columns from orig_seq
titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]
# Use .isin() to subset the rows of non_mus_tcks where tid is in the tid column of tracks_invoices.
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

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
# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

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
#Create a Boolean index, named boolean_filter, that selects rows from the left table with the job of 'Director' and avoids rows with the job of 'Director' in the right table.
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & (crews_self_merged['job_crew'] != 'Director'))

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
# check null values in a column and count them
null_budget = movies_financials['budget'].isnull()
number_of_missing_fin = null_budget.sum()
print(number_of_missing_fin)
#OR
# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()
# SUBSET ROWS WHERE COLUMN IS NULL (isnull)
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]
# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))

#Creating dict(From a list of dicts-row by row) or (From a dict of lists-column by column)
my_dict= {
    'Key1': 'value',
    'Key2': 'another. value',
    'Key3': 1952
}
#List of dict-by row(keys are the columns, values are the inputs per rows
l_o_dicts= [
    {'name':'ginger', 'breed':'Dash', 'height':22, 'weight':10, 'dob': '2019-03-14'},
    {'name':'scot', 'breed': 'dalma', 'height':59, 'weight':25, 'dob':'2019-05-09'}
]
new_dogs = pd.DataFrame(l_o_dicts)
#Dict of lists-by column
dict_o_l= {
    'name': ['ginger', 'scot'], 'breed':['Dash', 'dalma'], 'height': [22,59], 'weight':[10,25],
    'dob':['2019-03-14', '2019-05-09']
}
new_dogs = pd.DataFrame(dict_o_l)

# CSV to DataFrame
new_dogs = pd.read_csv('new_dogs.csv")
# DataFrame to CSV
new_dogs.to_csv('new_dogs_with_bmi.csv')

# merging = joining, tables = Dataframes (default= inner)
# Merging tables( join ward df on census df) this is inner join
wards_census = wards.merge(census, on= 'ward')
# add suffix to differentiate source of df during merge
wards_census = wards.merge(census, on= 'ward', suffixes=('_ward', '_cen'))
# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})
# Sort the counted_df in descending order
sorted_df = counted_df.sort_values(by= 'account', ascending= False)

#formula for merging 3 or more tables
df1.merge(df2, on= 'col')\.merge(df3, on= 'col')
# Group by ward, pop_2010, and vacant, then count the number of accounts
pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'], as_index=False).agg({'account': 'count'})

#LEFT JOIN merge
movies_taglines= movies.merge(taglines, on='id', how= 'left')
# MERGE WITH RIGHT JOIN
tv_movies = movies.merge(tv_genre, how='right', left_on='id', right_on= 'movie_id')
# OUTER JOIN
family_comedy = family.merge(comedy, on='movie_id', how='outer', suffixes=('_fam', '_com'))
# SELF JOIN (merge a table to itself, when: hierarchical and sequential relationship present)
original_sequels = sequels.merge(sequels, left_on= 'sequel', right_on= 'id', suffixes = ('_org', '_seq'))

# MERGING ON INDEXES
# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on='id', how='left')
# MULTIINDEX MERGE
samuel_casts = samuel.merge(casts, on=['movie_id', 'cast_id'])
# INDEX MERGE WITH LEFT_ON AND RIGHT_ON
movies_genres = movies.merge(movie_to_genres, left_on= 'id'
                             , left_index= True,
                             right_on= 'movie_id', right_index = True)

# FILTERING JOINS (SEMI JOIN) - filtering genres by what's in top tracks table
genres_tracks = genres.merge(top_tracks, on = 'gid')
top_genres = genres[genres['gid'].isin(genres_tracks['gid'])]
# ANTI JOIN STEPS
# 1 Merge genres and top_tracks
genres_tracks = genres.merge(top_tracks, on= 'gid', how = 'left', indicator= True)
#2# Select the gid column where _merge is left_only
gid_list = genres_tracks.loc[genres_tracks['_merge'] == 'left_only', 'gid']
#3 Get non top genres
non_top_genres = genres[genres['gid'].isin(gid_list)]

# Performing SEMI JOIN steps
# 1 Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')
# 2 Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]
# 3 Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})
# 4 Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))
# VALIDATING MERGES
.merge(validate='one_to_one' or 'one_to_many' or 'many_to_one' or 'many_to_many')

# CONCATENATE DF TOGETHER VERTICALLY
# BASIC CONCATENATION
pd.concat([inv_jan, inv_feb, inv_mar])
# IGNORING INDEX WHEN CONCATENATING (index goes from 0 to n-1
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index= True)
# Setting labels to original tables usign keys
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index= False, keys = ['jan', 'feb', 'mar'])
# CONCATENATE TABLES WITH DIFFERENT COLUMN NAMES default join is 'outer'
pd.concat([inv_jan, inv_feb], sort=True)
# concatenate matching columns9showing column names in 2 tables
pd.concat([inv_jan, inv_feb], join= 'inner')
# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})
# VERIFYING CONCATENATIONS (False is default value)
.concat(verify_integrity= False)

# USING MERGE_ORDERED() (default= outer) -- FOR ORDERED DATA/TIME SERIES, FILLING MISSING VALUES
pd.merge_ordered(aapl, mcd, on= 'date', suffixes=('_aapl', '_mcd'))
# FORWARD FILL TO FILL MISSING WITH PREVIOUS VALUE
pd.merge_ordered(aapl, mcd, on= 'date', suffixes=('_aapl', '_mcd'), fill_method= 'ffill')
# Using merge_ordered om multiple columns
date_ctry = pd.merge_ordered(gdp, pop, on=['country', 'date'], fill_method= 'ffill')
# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on= 'year', right_on='date', how='left')
#Subset the gdp_sp500 table, select the gdp and returns columns, and save as gdp_returns
gdp_returns = gdp_sp500[['gdp', 'returns']]

# MERGE_ASOF() - similar to merge_ordered() left join, match on equal to or nearest value
# USE MERGE_ASOF() WHEN- DATA SAMPLED FROM A PROCESS, DEVELOPING A TRAINING SET(NO DATA LEAKAGE)
pd.merge_asof(visa, ibm, on='date_time', suffixes=('_visa', '_ibm'))
# use direction argument 'forward' to select 1st row on right table whose 'on' key column is greater than or equal to left keys column, use 'nearest' where rows with nearest timees are matched
pd.merge_asof(visa, ibm, on=['date_time'], suffixes=('_visa', '_ibm"), direction='forward')      

# Using merge_asof() to create dataset STEPS
# 1 Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp,recession, on='date')
# 2 Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]
# 3 Plot a bar chart of gdp_recession
dp_recession.plot(kind='bar', y='gdp', x='date', color=is_recession, rot=90)
plt.show()

# RESHAPING DATA WITH .MELT() id_vars= columns from original dataset we don't want to change
social_fin_tall = social_fin.melt(id_vars=['financial','company'])
# MELTING WITH VALUE_VARS, value_vars argument allows controlling which columns are unpivoted
social_fin_tall = social_fin.melt(id_vars=['financial','company'], value_vars=['2018','2017')
# MELTING WITH COLUMN NAMES
social_fin_tall = social_fin.melt(id_vars=['financial','company'], value_vars=['2018','2017'], var_name='year', value_name='dollars')

# SELECTING DATA WITH .QUERY()
# QUERYING ON SINGLE CONDITION
stocks.query('nike >= 90')
# QUERYING ON MULTIPLE CONDITIONS
stocks.query('nike > 90 and disney <140')
stocks.query('nike > 96 or disney < 98')
# USING QUERY TO SELECT TEXT
stocks_long.query('stock=="disney" or (stock==="nike" and close < 90)')

# calculate column range using range fucntion
def range(column):
    return column.max() - column.min()
print(sales['unit_price'].agg(range)

# Compute price diff 1
price_diffs = jpm_wells_bac.diff()
# Plot the price diff of the close of jpm, wells and bac only 2
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()

#ADD COLUMN FOR NAME LENGTH
#most efficient way to do what is above
brics["name_length"] = brics["country"].apply(len)
print(brics)

               
