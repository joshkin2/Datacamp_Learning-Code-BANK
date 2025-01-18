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















               
