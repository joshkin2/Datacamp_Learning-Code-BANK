
#NUMPY LOGIC
# to compare values in NumPy
np.logical_and(bmi > 21, bmi < 22)
np.logical_or(bmi > 21, bmi < 22)
np.logical_not(bmi > 21, bmi < 22)
# to see the digits for the above instead, use
bmi[np.logical_and(bmi > 21, bmi < 22)

#LIST
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
#calculate length of string and list
string_length = len('hello, world')
list_length = len([1,2,3,4,5])


#SET
#convert list to set
new_variable = set(variable)
#extracting comonality between sets
new_set = set1 & set2
#union of set
set1.union(set2)
#check if a set is a subset(is new_set a subset of set1?)
new_set.issubset(set1)


#FUNCTIONS
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

#Exception handling
#types of errors. use try and except blocks to prevent program crash
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

#CREATING A CLASS
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

#OPENING FILES
#- 'r' to read file only, 'w' to write
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


#using dot
u = np.array([1,2])
v = np.array([3,1])
result = np.dot(u,v)
result is 5(1*3+2*1=5)



#reading JSON files
import json
with open('filesample.json', 'r') as openfile:
    json_object = json.load(openfile)
print(json_object)


                   
#custom fucntion using agg on multiple columns
def iqr(column):
    return column.quantile(0.75) - column.quantile(o.25)
print(sales["temperature_c", "fuel", "unemployment"].agg(iqr))   #to calculate it with median we can edit ".agg([iqr, np.median])"


#how to ignore warnings
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)    #ignore all warnings


