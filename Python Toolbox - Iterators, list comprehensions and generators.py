 # ITERATING over iterables: NEXT() - prints each letter one by one
word= 'Da'
it = iter(word)
next(it)
# ITEATING AT ONCE WITH *
word = 'Data'
it = iter(word)
print(*it)
# ITERATING DICT
pythonistas= {'hugo':'bowne', 'francis':'castro'}
for key, vlaue in pythonistas.items():
  print(key, value)
# ITERATING OVER FILE CONNECTIONS
file = open('file.txt')
it= iter(file)
print(next(it))
# EXERCISE
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
# Print each list item in flash using a for loop
for person in flash:
    print(person)
# Create an iterator for flash: superhero
superhero= iter(flash)
# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

# EXERCISE 2
# Create an iterator for range(3): small_value
small_value = iter(range(3))
# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))
# Loop over range(3) and print the values
for n in range(3):
    print(n)
# Create an iterator for range(10 ** 100): googol
googol = iter(range(10**100))
# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

# EXERCISE 3
# Create a range object: values
values = range(10,21)
# Print the range object
print(values)
# Create a list of integers: values_list
values_list = list(values)
# Print values_list
print(values_list)
# Get the sum of values: values_sum
values_sum = sum(values)
# Print values_sum
print(values_sum)

# USING ENUMERATE()
movies= ['chucky','WS', 'atlanta']
e= enumerate(avengers)
print(type(e))
e_list=list(e)
print(e_list)  #print elements of iterable and index within it

# enumerate() and unpack
for index,value in enumerate(avengers): #to start index at any number insert ",start=10" in enumerate()
  print(index,value)

# USING ZIP
movies= ['chucky','WS', 'atlanta']
names= ['danger', 'action', 'drama']
z= zip(movies, names)
print(type(z))
z_list= list(z)
print(z_list)

# zip() and unpack
for z1,z2 in zip(movies, names):
  print(z1,z2)
# print zip with *
z = zip(movies,names)
print(*z)

#EXERCISE 1
# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))
# Print the list of tuples
print(mutant_list)
# Unpack and print the tuple pairs
for index1,value1 in enumerate(mutants):
    print(index1, value1)
# Change the start index
for index2,value2 in enumerate(mutants, start=1):
    print(index2, value2)
# EXERCISE 2
# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))
# Print the list of tuples
print(mutant_data)
# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases,powers)
# Print the zip object
print(mutant_zip)
# Unpack the zip object and print the tuple values
for value1,value2,value3 in (mutant_zip):
    print(value1, value2, value3)

# EXERCISE 3 --- Using * and zip to 'unzip'
# Create a zip object from mutants and powers: z1
z1 = zip(mutants,powers)
# Print the tuples in z1 by unpacking with *
print(*z1)
# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants,powers)
# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)
# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)

# ITERATORS TO LOAD LARGE FILES INTO MEMORY
import pandas as pd
result= []
for chunk in pd.read_csv('data.csv',chunksize=1000):
  result.append(sum(chunk['x']))
total = sum(result)
print(total)   # this gives sum of a column x
# OR
import pandas as pd
total= 0
for chunk in pd.read_csv('data.csv',chunksize=1000):
 total+=sum(chunk['x'])
print(total)
# EXERCISE 1
# Initialize an empty dictionary: counts_dict
counts_dict= {}
# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv',chunksize=10):
    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1
# Print the populated dictionary
print(counts_dict)

# EXERCISE
# Define count_entries()
def count_entries(csv_file,c_size,colname):
    """Return a dictionary with counts of
    occurrences as value for each key.""" 
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}
   # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file,chunksize=c_size):
        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    # Return counts_dict
    return counts_dict
# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv',10,'lang')
# Print result_counts
print(result_counts)

# LIST COMPREHENSIONS
nums= [12,8,21,3,16]  # sampe 1
new_nums= [num + 1 for num in nums]
print(new_nums)
result= [num for num in range(11)]  # sample 2
print(result)
pairs_2= [(num1,num2) for num1 in range(0,2) for num2 in range(6,8)]  #sample 3
print(pairs_2)
first_letters= [doc[0] for doc in doctor]
valjean= 24601   # list comprehension can't be built over integer object
# Create list comprehension: squares
squares = [i**2 for i in range(0,10)]
print(squares)

# NESTED LIST COMP.
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for col in range(0,5)] # col is iterator variable
# Print the matrix
for row in matrix:  # row is iterator variable
    print(row)

# CONDITIONALS IN COMP - ON THE ITERABLE
[num ** 2 for num in range(10) if num % 2 ==0] #returns even numbers only
# CONDITIONALS IN COMP - ON THE OUTPUT EXPRESSION
[num ** 2 if num%2==0 else 0 for num in range(10)] # replaces odd numbers with 0
# DICT COMP - CREATE DICTS
pos_neg= {num: -num for num in range(9)} # +ve keys -ve vale
print(pos_neg)

# EXERCISE 1
# members of fellowship that have 7 characters or more
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member)>6]
# Print the new list
print(new_fellowship)

# EXERCISE 2
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create list comprehension: new_fellowship
new_fellowship = [member if len(member)>=7 else "" for member in fellowship]
# Print the new list
print(new_fellowship)

# EXERCISE 3
# dictionary with members as keys and length of string as values
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}
# Print the new dictionary
print(new_fellowship)

# PRINTING FROM GENERATORS
# generators use ()
# list comp use []
result= (num for num in range(6))
for num in result:
 print(num)
 #OR
result= (num for num in range(6))
print(list(result))
#OR
result= (num for num in range(6))
print(next(result))
print(next(result))
print(next(result)) # prints the first 3 values

#CONDITIONALS IN GENERATOR EXPRESSIONS
even_nums= (num for num in range(10) if num % 2==0)
print(list(even_nums))

#GENERATOR FUNCTION
def num_sequence(n):
 """Generate values from 0 to n"""
 i= 0
 while i<n:
  yield i
  i+=1
# USE GENERATOR FUNCTION
result= num_sequence(5)
print(type(result))
fpr item in result:
print(item)

#EXERCISE 1
# Create generator object: result
result = (num for num in range(0,31))
# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# Print the rest of the values
for value in result:
    print(value)

# EXERCISE 2
# extract length of values from list
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
# Create a generator object: lengths
lengths = ( len(person) for person in lannister)
# Iterate over and print the values in lengths
for value in lengths:
    print(value)
#EXERCISE 3
# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""
    # Yield the length of a string
    for person in input_list:
      yield len(person)
# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)

#EXERCISE 4 -extract time from time-stamped Twitter data
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']
# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]  #12th to 19th characters in the string to extract the time
# Print the extracted times
print(tweet_clock_time)

#EXERCISE 5
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']
# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']
# Print the extracted times
print(tweet_clock_time)









