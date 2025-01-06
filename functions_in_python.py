# DEFINING A FUNCTION
def square():
  new_value= 4**2
  print(new_value)
square()
# Function parameters- get square of any value
def square(value):
  new_value= value**2
  print(new_value)
square(4)
# return value from functions
def square(value):
  new_value= value**2
  return new_value
num= square(4)
print(num)
# Docstrings describes what function does and is btw triple double quotes
def square(value):
  """Returns the square of a value"""
  new_value= value**2
  return new_value
  
  # Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word='congratulations'+'!!!'
    # Print shout_word
    print(shout_word)
# Call shout
shout()

# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'
    # Print shout_word
    print(shout_word)
# Call shout with the string 'congratulations'
shout('congratulations')

#MULTIPLE FUNCTION PARAMETERS
def raise_to_power(value1,value2):
  """Raise value1 to power of value2"""
  new_value= value1 ** value2
  return new_value
"""call function"""
result= raise_to_power(2,3)
#unpacking tuples into several variables
even_nums=(2,4,6)
a,b,c= even_nums
# RETURNING MULTIPLE VALUES
def raise_both(value1,value2):
  """Raise val1 to power of val2 and viceversa"""
  new_val1=value1**value2
  new_val2=value2**value1
  new_tuple=(new_val1,newval2)
  return new_tuple
  
# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):  
    # Concatenate word1 with '!!!': shout1
    shout1=word1+"!!!"
    # Concatenate word2 with '!!!': shout2
    shout2=word2+"!!!"
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words= (shout1,shout2)
    # Return shout_words
    return shout_words
# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1,yell2=shout_all("congratulations","you")
# Print yell1 and yell2
print(yell1)
print(yell2)

#build dictionary: keys are names of languages and values are number of tweets 
# Import pandas
import pandas as pd
# Import Twitter data as DataFrame: df
df = pd.read_csv("tweets.csv")
# Initialize an empty dictionary: langs_count
langs_count = {}
# Extract column from DataFrame: col
col = df['lang']
# Iterate over lang column in DataFrame
for entry in col:
    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
       langs_count[entry] +=1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry]=1
# Print the populated dictionary
print(langs_count)

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    # Initialize an empty dictionary: langs_count
    langs_count = {}
    # Extract column from DataFrame: col
    col = df["lang"]   
    # Iterate over lang column in DataFrame
    for entry in col:
        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry]+=1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry]=1
    # Return the langs_count dictionary
    return langs_count
# Call count_entries(): result
result=count_entries(tweets_df,"lang")
# Print the result
print(result)

# SCOPE= PART OF PROGRAM WHERE OBJECT/NAME MAY BE ACCESSIBLE
# TYPES= GLOBAL- DEFINED IN MAIN BODY OF SCRIPT, LOCAL- DEFINED INSIDE A FUNCTION
#BUILT-IN- NAMES IN PRE-DEFINED BUILT-INS MODULE eg. PRINT(),Enclosed Functions
new_val = 10
def square(value):
  global new_val
  new_val= new_val ** 2
  return new_val

#keyword global within function to alter value of variable defined in global scope
team="teen titans"
def change_team():
  global team
  team="justice league" # Change the value of team in global: team
print(team)
change_team() # Call change_team()
print(team)

# NESTED FUNCTIONS - to use process a no of times within function
def mod2plus5(x1,x2,x3):
  """returns remainder plus 5 of three values"""
  def inner (x):
    """returns remainder plus 5 of a value"""
    return x % 2 + 5
  return (inner(x1), inner(x2),inner(x3))
  print(mod2plus5(1,2,3))

# return nth power of any number
def raise_val(n):
  """return inner function"""
  def inner(x):
    """raise x to power of n"""
    raised= x ** n
    return raised
  return inner
square= raise_val(2)
cube=raise_val(3)
print(square(2), cube(4))
# USING NONLOCAL
def outer():
  """prints value of n"""
  n=1
  def inner():
    nonlocal n
    n=2
    print(n)
  inner()
  print(n)

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""
    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))
# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

# Define echo
def echo(n):
    """Return the inner_echo function."""
    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word
    # Return inner_echo
    return inner_echo
# Call echo: twice
twice = echo(2)
# Call echo: thrice
thrice= echo(3)
# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

#using nonlocal withi =n nested function to alter value of variable in enclosed scope
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable""" 
    # Concatenate word with itself: echo_word
    echo_word= word + word   
    # Print echo_word
    print(echo_word)  
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word+"!!!"  
    # Call function shout()
    shout()
    # Print echo_word
    print(echo_word)
# Call function echo_shout() with argument 'hello'
echo_shout("hello")































