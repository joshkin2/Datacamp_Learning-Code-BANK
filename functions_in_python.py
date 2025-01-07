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

# FLEXIBLE ARGUMENTS *ARGS variable-length arguments
def add_all(*args):
  """sum all values in *args together"""
  #Initialize sum
sum_all=0
# accumulate the sum
for num in args:
  sum_all += num
return sum_all
add_all(1,2) # will print out 3

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""
    # Initialize an empty string: hodgepodge
    hodgepodge=""
    # Concatenate the strings in args
    for word in args:
        hodgepodge += word
    # Return hodgepodge
    return hodgepodge
# Call gibberish() with one string: one_word
one_word = gibberish("luke")
# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")
# Print one_word and many_words
print(one_word)
print(many_words)

#**KWARGS - variable-length keyword arguments
def print_all(**kwargs):
  """print out key-value pairs in **kwards"""
  #print out key-value pairs
for key, value in kwargs.items():
  print(key+":"+value)
print_all(name="duds",job="hero")

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)
    print("\nEND REPORT")
# First call to report_status()
report_status(name="luke",affiliation="jedi",status="missing")
# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")

#Functions with 1 defaut argument
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1*echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # Return shout_word
    return shout_word
# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")
# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey",echo=5)
# Print no_echo and with_echo
print(no_echo)
print(with_echo)

# FUNCTIONS WITH MULTIPLE DEFAULT ARGUMENTS
# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'
    # Return echo_word_new
    return echo_word_new
# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey",echo=5,intense=True)
# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey",intense=True)
# Print values
print(with_big_echo)
print(big_no_echo)

# GENERALIZED TWITTER LANGUAGE ANALYSIS - With 1 column name
# Define count_entries()
def count_entries(df, col_name="lang"):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Extract column from DataFrame: col
    col = df[col_name]
    # Iterate over the column in DataFrame
    for entry in col:
        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
    # Return the cols_count dictionary
    return cols_count
# Call count_entries(): result1
result1 = count_entries(tweets_df,"lang")
# Call count_entries(): result2
result2 = count_entries(tweets_df,col_name="source")
# Print result1 and result2
print(result1)
print(result2)

# GENERALIZED TWITTER LANGUAGE ANALYSIS - With mltiple column names
# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""  
    #Initialize an empty dictionary: cols_count
    cols_count = {}    
    # Iterate over column names in args
    for col_name in args:    
        # Extract column from DataFrame: col
        col = df[col_name]   
        # Iterate over the column in DataFrame
        for entry in col:    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1 
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    # Return the cols_count dictionary
    return cols_count
# Call count_entries(): result1
result1 = count_entries(tweets_df, "lang")
# Call count_entries(): result2
result2 = count_entries(tweets_df, "lang", "source")
# Print result1 and result2
print(result1)
print(result2)
























