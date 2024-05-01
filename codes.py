# plot histogram, scatterplot, graph
plt.hist(x,y), plt.scatter(x,y), plt.plot(x,y)
# display graph- nothing goes in parenthesis
plt.show()
# build histogram with 5 bins. few bins= oversimplicity, too many bins= overcomplicate and hinder bigger picture
plt.hist(x or y, bins=5)
# clean up plot
plt.clf()
# labelling graphs, adding title, starting y from zero
plt.xlabel("year")
plt.ylabel("population")
plt.title("World Population Projections")
plt.yticks([0,2,4,6,8,10])
plt.show()
# add data to graph source
year = [1800 ,1850 ,1900] + year
pop = [1.0, 1.262, 1.650] + pop
# import decision trees scikit-learn libraries
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion matrix
# changing opasity of colors in  the argument inside plt.scatter()
(alpha = 0.8) #zero is transparent, one is not at all transparent
# to add grid to plot
plt.grid(True)
## Dictionary Datacamp Lecture
#To get position of a value in a list use
new variable = variablethatcontainsvalueneeded.index("value you're looking for")
# converting lists to dictionaries
pop = [30.55, 2.77, 39.21] # list
countries = ["afghan", "albania", "algeria"] # list
world = {"afghan":30.55, "albania":2.77. "algreria":39.21} # dict
# to find value of albania in dict use
world["albania"]
# get the index of albania in list
ind_albania = countries.index("albania")
# to print out keys
print(europe.keys())		
# add more data to dict or update an info in dict
world["sealand"] = int, float or str                           
# check if a value is in a dict
"sealand" in world
# delete value from dict
del(world["sealand"])
#chain square brackets to select elements
europe['spain']['population']
# Correct way to add a key-value pair to a dictionary
data = {'capital': 'rome', 'population': 59.83}
europe['italy'] = data
print(europe)
#turn dict into dataframe called cars
cars = pd.DataFrame(my_dict)
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
#extracting fro, beginning to end
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
# to compare values in NumPy
np.logical_and(bmi > 21, bmi < 22)
np.logical_or(bmi > 21, bmi < 22)
np.logical_not(bmi > 21, bmi < 22)
# to see the digits for the above instead, use
bmi[np.logical_and(bmi > 21, bmi < 22)
#if, elif, else (conditional statements)
z = 4
if z % 2 == 0 : #True
    print("z is even")
# if z is not equal to 0 then else conditon comes in below print 
else :
    print("z is odd")
# using elif
z = 3
if z % 2 == 0 :
    print('z is divisible by 2') #False
elif z % 3 == 0 :
    print('z is divisible by 3') #True( if the condition at the top is met, then this line of code won't be executed
else :
    print('z is neither divisible by 2 not by 3')
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
# using while loop
error = 50.0
while error > 1:
    error = error/4
    print(error)  #this wil make error keep getting divided by 4 till it gets to "1"
#concatenation
concantenated_string = string1 + string2
result = "Hello" + "John"</td>    #example of concatenation
#slicing format
substring = string_name[start:end]
#clone list
vairable = [elemtents]
new_variable = variable[:]
# delete element from list
del(variable[index number]) delvarianle[index number] #one of both
#add element to end of list
variable.append(element)
#count number of occurences of an element in a list
count = variable.count(element)
#add multiple elements to a list
main_variable.extend(variable_containing_elements_to_be_added_to_main_variable)
#another way to remove element from a list
new_variable = variable.pop(index no)
#remove element from a list
variable.remove(index no)
#reverse order of a list
variable.reverse()
#sort elements in list in ascending or descending order
variable.sort() or variable.sort(reverse = True)
#delete key from a dict
del dict_name[key]
#to see all the keys in a dict
dict.keys()
#see all values in a dict
dict.values()
#extract keys in a dict as a list
list(dict.keys())















