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
#ifelse
age = 17
if(age>18):
    print('you will enter')
else:
    print('access denied')
print(move on)
#elif
if(age>18):
    print('you will enter')
elif(age==18):
    print('go in')
else:
    print('access denied')
print('move on')
#and operator
False and False = False
False and True = False
True and False = False
True and True = True
#or operator
False or Flase = False
False or True = True
True or False = True
True or True = True
#counting 1-10 with for loop
for number in range(1,11):
    print(number)
#to keep track of both the item and its position in a list
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)
#to print out every element in a list
dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])
# Use for loop to change the elements in list(changes all colors to white)
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])
#display values of rating of an album playlist stored in PlayListRatings
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]
while(i < len(PlayListRatings) and rating >= 6):
    print(rating)
    i = i + 1 
    rating = PlayListRatings[i]  
#extract animals with 7 letters
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
New = []
i=0
while i<len(Animals):
    j=Animals[i]
    if(len(j)==7):
        New.append(j)
    i=i+1
print(New)
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
#convert list to set
new_variable = set(variable)
#extracting comonality between sets
new_set = set1 & set2
#union of set
set1.union(set2)
#check if a set is a subset(is new_set a subset of set1?)
new_set.issubset(set1)
#to access index info of list elements using for loop
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for index, area in enumerate(areas):
    print("room" + str(index) + ":" + str(area))
#indexing above will start from 0, to make it start from 1 use
print("room" + str(index+1) + ":" + str(area))
#sample of the abpve
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm")
#print out elemenets in a dict using for loop(output may be unordered)
world = {"ghana":20,
         "usa": 2.5.
         "nigeria":23}
for key, value in world.items():
    print(key + "--" + str(value))
#print out elements in a Numpy arrays using for loop
for val in bmi:
    print(val)
#print out elemenets in a 2D Numpy arrays using for loop
for val in np.nditer(variable name) :
    print(val)
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
#random generators
np.random.seed(123)
np.random.rand()
#coin toss game
import numpy as np
np.random.seed(123)
coin = np.random.randint(0,2)
print(coin)
if coin == 0:
    print("heads")
else:
    print("tails")
#generate and print random float after setting seed
print(np.random.rand())
#simulate a dice(number will start from 1 and end at 7-1=6)
print(np.random.randint(1,7)
#using distribution to calculate odds
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails = []
for x in range(100) :
    tails = [0]
    for x in range(10) :
    coin = np.random.randint(0, 2)
    tails. append(tails[x] + coin)
final_tails.append(tails[-1])
plt.hist(final_tails, bins = 10)
plt.show()
#proper way to set up random ops with for-if-else
import numpy as np
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0,2)
    if coin ==0:
        outcomes.append('heads')
    else:
        outcoes.append('tails')
print(outcomes)
#doing the above using random walk
np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0,2)
    tails.append(tails[x] + coin)
print(tails)
#more example of the above 
# Initialize random_walk EG
random_walk = [0]
for x in range(100) :
# Set step: last element in random_walk EG
step = random_walk[-1]
# Roll the dice EG
dice = np.random.randint(1,7)
# Determine next step EG
if dice <= 2:
    step = step - 1
elif dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1,7)
# append next_step to random_walk EG
random_walk.append(step)
# Print random_walk EG
print(random_walk)
# to make sure that a variable x never goes below 10 when you decrease it, you can use:
step = max(0, step -1) 
#example 
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)
# Convert all_walks to NumPy array: np_aw EG
np_aw = np.array(all_walks)
# Plot np_aw and show EG
plt.plot(np_aw)
plt.show()
# Clear the figure EG
plt.clf()
# Transpose np_aw: np_aw_t EG
np_aw_t = np.transpose(np_aw)
# Plot np_aw_t and show EG
plt.plot(np_aw_t)
plt.show()
# EXAMPLE
# Simulate random walk 500 times EG
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
# Create and plot np_aw_t EG
np_aw_t = np.transpose(np.array(all_walks))
# Select last row from np_aw_t: ends EG
ends = np_aw_t[-1,:]
# Plot histogram of ends, display plot EG
plt.hist(ends)
plt.show()
#calculate length of string and list
string_length = len('hello, world')
list_length = len([1,2,3,4,5])
#to define functions use def
def greet(name):
    print('Hello, ' + name)
result = greet('Alice')
print(result)
#functions and loops
def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)
print_numbers(5)













