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





















