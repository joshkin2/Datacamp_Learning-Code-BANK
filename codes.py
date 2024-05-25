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
#print each element in a list using fucntion and for loop
def Printlist(the-list):
    for element in the_list:
        print(element)
Printlist(['1',1,'the man','abc'])
# Python Program to Count words in a String using Dictionary
def freq(string, counted_word): 
#step1: A list variable is declared and initialized to an empty list. EG
    words = []
#step2: Break the string into list of words EG
    words = string.split() # or string.lower().split()
#step3: Declare a dictionary EG
    Dict = {}
#step4: Use for loop to iterate words and values to the dictionary EG
    for key in words:
        if (key == counted_word):
            Dict[key] = words.count(key)
#step5: Print the dictionary EG
    print("The Frequency of words is:",Dict)
#step6: Call function and pass string in it EG
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb. Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go", "counted_word")
# Example of global variable
myFavouriteBand = "AC/DC"
def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)
# Example of local variable
def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)
#Exception handling: types of errors. use try and except blocks to prevent program crash
try:
    result= 10/ 0
except ZeroDivisionError:
    print('Error: Cannot  divide by zero')
print('outside of try and except block')
#example of using try, except, finally for exception handling
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
#another example using function
def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
        return None
numerator = int(input('Enter numerator value: '))
denominator = int(input('Enter denominator value: '))
print(safe_divide(numerator,denominator))
#creating a class
class ClassName:
    class_attribute = value
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    def method1(self, parameter1, parameter2, ...):
# an example of the above
class Car:
    max_speed = 120
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed
    def get_speed(self):
        return self.speed
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")
car1.accelerate(30)
car2.accelerate(20)
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")
#another example of the above
import matplotlib.pyplot as plt
%matplotlib inline
# Create a class Circle to draw an actual circle
class Circle(object):
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
#to draw the object
RedCircle.drawCircle()
#add to radiius of cicle
RedCircle.add_radius(2)
# create class rectangle for an actual rectangle(width, height and color are the attributes)
class Rectangle(object):
    def __init__(self, width=2, height=3, color='r'):
        self.width = width
        self.height = height
        self.color = color
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()
SkinnyBlueRectangle = Rectangle(2,3,'blue')
#last example of the above(Scenario: Car dealership's inventory management system)
class Vehicle:
    color = "white"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity
    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)
vehicle1 = Vehicle(200, 20)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()
vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()
#opening files- 'r' to read file only, 'w' to write
with open('Example1.txt','r') as file1:
    file_stuff=file1.read()
    print(file_stuff)
print(file1.closed)
print(file_stuff)
#ouput every line in a file as an element in a list
file_stuff=file1.readline()
print(file_stuff)
#copy one file to a new file
with open('Example1.txt','r') as readfile:
    with open('Example3.txt', 'w') as writefile:
        for line in readfile:
            writefile.write(line + '\n')
#cleaning data and appending the file
<details><summary>Click here for the solution</summary>
```python
def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            header = members[0]
            members.pop(0)
            inactive = [member for member in members if ('no' in member)]
            '''
            The above is the same as 

            for member in members:
            if 'no' in member:
                inactive.append(member)
            '''
            #go to the beginning of the write file
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()                
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)
# code to help you see the files
headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
```
</details>
#pandas: Loading Data
df.loc['a', 'Artist']      #to access the name of the artist in row a, colum artist
#save as CSV
df1.to_csv('new_songs.csv')
#create a Series from a list
data = [10,2,4,5]
s = pd.Series(data)
print(s)
#assessing 3rd row by position
print(df.iloc[2])
#assessing 2nd row by label
print(df.loc[1])
#extract data of ages more than 25 in a DF
high_above_25 = df[df['Age'] > 25]
#using dot
u = np.array([1,2])
v = np.array([3,1])
result = np.dot(u,v)
result is 5(1*3+2*1=5)
#calculate mean for a colum in a DF
games_home['PLUS_MINUS'].mean()
#requests
import requests
url = 'https://www.sample.com/'
r = requests.get(url)
r.status_code : 200
#WEB SCRAPING 
#import Beautiful Soup to parse thr web page content EG
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
# Specify the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/IBM'
# Send an HTTP GET request to the webpage
response = requests.get(url)
# Store the HTML content in a variable
html_content = response.text
# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# Display a snippet of the HTML content EG
print(html_content[:500])
#pandas read_html for table extraction
read_html()
#extracting tables from webpages
import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
tables = pd.read_html(URL)
df = tables[0]   or use df = tables(2)     #required table will have index 2
print(df)
#reading JSON files
import json
with open('filesample.json', 'r') as openfile:
    json_object = json.load(openfile)
print(json_object)
#reading XML files
import pandas as pd
import xml.etree.ElementTree as etree
tree = etree.parse('fileExample.xml')
root = tree.getroot()
columns = ['Name', 'Phone Number', 'Birthday']
df = pd.DataFrame(columns = columns)
for node in root:
    name = node.find('name').text
    phonenumber = node.find('phonenumber').text
    birthday = nod.find('birthday').text
    df = df.append(pd.Series([name, phonenumber, birthday],
    index = columns)....., ignore_index = True
#applying transform to a DF
df = df.transform(func = lambda x : x + 10)
print(df)
#find sqt of each element in the DF
result = df.transform(func = ['sqrt]')
#SAMPLE OF WEBSCRAPING
import requests
from bs4 import BeautifulSoup
page = requests.get('http://EnterWebsiteURL'...).text
#creates a BeautifulSoup object   EG
soup = BeautifulSoup(page, 'html.parser')
#pulls all instances of <a> tag
artists = soup.find_all('a')
#clears data of all tags
for artist in artists:
    names = artist.contents[0]
    fullLink = artist.get('href')
    print(names)
    print(fullLink)
#to perform webscraping we need to install these libraries with the codes
!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
!pip install requests==2.26.0
#to import modules and functions for webscraping
from bs4 import BeautifulSoup
import requests
#parse html through BS constructor
soup = BeautifulSoup(html, 'html.parser')
#display html in nested structure
print(soup.prettify())
#Downloading And Scraping The Contents Of A Web Page
url = 'http://www.ibm.com'
#We use get to download the contents of the webpage in text format and store in a variable called data   EG
data = requests.get(url).text
#We create a BeautifulSoup object using the BeautifulSoup constructor
soup = BeautifulSoup(data.'html.parser')
#Scrape all links
for link in soup.find_all('a' .href=True):
    print(link.get('href'))     # in html anchor/link is represented by the tag <a>
#Scrape all images Tags
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))    
#Scrape data from HTML tables    EG
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.htm
#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
Before proceeding to scrape a web site, you need to examine the contents, and the way data is organized on the website. Open the above url in your browser and check how many rows and columns are there in the color table.
#get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>
#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))
#Scrape data from HTML tables into a DataFrame using BeautifulSoup and Pandas
import pandas as pd
#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"
Before proceeding to scrape a web site, you need to examine the contents, and the way data is organized on the website. Open the above url in your browser and check the tables on the webpage.
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>
# we can see how many tables were found by checking the length of the tables list
len(tables)
#Assume that we are looking for the 10 most densly populated countries table, we can look through the tables list and find the right one we are look for based on the data in each table or we can search for the table name if it is in the table but this option might not always work.
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
#See if you can locate the table name of the table, 10 most densly populated countries, below.
print(tables[table_index].prettify())
population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])
​for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)
​population_data
#Scrape data from HTML tables into a DataFrame using BeautifulSoup and read_html
#Using the same url, data, soup, and tables object as in the last section we can use the read_html function to create a DataFrame.
#Remember the table we need is located in tables[table_index]
#We can now use the pandas function read_html and give it the string version of the table as well as the flavor which is the parsing engine bs4.
pd.read_html(str(tables[5]), flavor='bs4')
#The function read_html always returns a list of DataFrames so we must pick the one we want out of the list.
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]
​population_data_read_html
#Scrape data from HTML tables into a DataFrame using read_html
#We can also use the read_html function to directly get DataFrames from a url.
dataframe_list = pd.read_html(url, flavor='bs4')
#We can see there are 25 DataFrames just like when we used find_all on the soup object.
len(dataframe_list)
#Finally we can pick the DataFrame we need out of the list.
dataframe_list[5]
#We can also use the match parameter to select the specific table we want. If the table contains a string matching the text it will be read.
pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
#download historical stock prices using yfinance
import yfinance as yf
#download historical data for a stock    EG
msft = yf.Ticker('MSFT')      #AKA microsoft
msft_data = msft.history(period='max')
#display the downloaded data
masft_data.head()
country = usa
sector = technology
#how to ignore warnings
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)    #ignore all warnings
#Steps for extracting the data from webpage using web scraping
#1:  send http request to web page
url = 'https://sample.html'
data = requests.get(url).text
print(data)
#2:  Parse the HTML content with BeautifulSoup library
soup = BeautifulSoup(data, 'html5lib')
#3:  Identify HTML tags and covert table in webpage to DF
netflix_data = pd.DataFrame(columns=['Date','Open', 'High', 'Low', 'Close', 'Volume'])
#4:  Use a BeautifulSoup method for extracting data
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    
#    Print the extracted data
netflix_data.head()
#Steps for Extracting data using pandas library
#1:
read_html_pandas_data = pd.read_html(url)
# or convert the BeautifulSoup object to a string
read_html_pandas_data = pd.read_html(str(soup))
#since it's just one table in the page we're using 0 but if it was another table we'd use the specific number
netflix_dataframe = read_html_pandas_data[0]
netflix_dataframe.head()
# print last row of DF
last_row = amazon.data.tail(1)
print(last_rows)
# reset index
netflix_data.reset_index(inplace=True)
#print 2D numpy array values
print(variablename.values)
#print index of columns: col names
print(variablename.columns)
#print index for the rows:row numbers or names
print(variablename.index)
#subsetting rows
dogs[dogs['height_cm'] > 50]
#sort 1 column(smallest to largest)
df.sort_values('column_name', ascending= False)
#sort multiple columns
df.sort_values(['column_name1', 'column_name2'])
#EG of sort multiple colums
home_fam = house.sort_values(['region','family'], ascending=[True,False])
#select multiple columns of a DF
df[['col_a', 'col_b']]
#filtering or selecting rows
dogs[dogs['height_cm'] > 60]
#filtering or selecting rows under multiple conditions [for and or condition use "|"]
dogs[(dogs['height_cm'] > 60) & (dogs['color'] == 'tan')]
#subsettin rows by categorical variables using .isin() method. homelessness is the DF
canu = ["California", "Arizona", "Nevada", "Utah"]
mojave_homelessness = homelessness["state"].isin(canu)
homelessness[mojave_homelessness]
print(mojave_homelessness)
#Adding new column
dogs['height_m'] = dogs['height_cm'] / 100
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
#mean, median, min, max of column in a DF
print(sales["weekly_sales"].mean())
#custom fucntion using agg on multiple columns
def iqr(column):
    return column.quantile(0.75) - column.quantile(o.25)
print(sales["temperature_c", "fuel", "unemployment"].agg(iqr))   #to calculate it with median we can edit ".agg([iqr, np.median])"

















