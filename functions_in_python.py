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

def extract_emails(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text= f.read()
        email_patt= r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails=re.findall(email_patt,text)
        return emails
filename= 'data\email_exchanges_big.txt'
print(extract_emails(filename))

#LAMBDA FUNCTIONS
raise_to_power= lambda x,y:x**y
raise_to_power(2,3)
# ANONYMOUS FUNCTIONS
nums= [1,2,3,4,5]
square_all= map(lambda num:num**2, nums)
print(square_all) # to see the object
print(list(square_all)) # to see what it contains
# EXERCISE
# Define echo_word as a lambda function: echo_word
echo_word = lambda word1,echo:word1*echo
# Call echo_word: result
result = echo_word('hey',5)
# Print result
print(result)
# EXERCISE
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]
# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item:item+'!!!', spells)
# Convert shout_spells to a list: shout_spells_list
shout_spells_list= list(shout_spells)
# Print the result
print(shout_spells_list)
# EXERCISE - a new list that contains only strings that have more than 6 characters.
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member)>6, fellowship)
# Convert result to a list: result_list
result_list=list(result)
# Print result_list
print(result_list)
# EXERCISE - takes a list of strings as an argument and returns, as a single-value result, the concatenation of all of these strings.
# Import reduce from functools
from functools import reduce
# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1,item2:item1 + item2, stark)
# Print the result
print(result)

#ERROR HANDLING
#EXCEPTIONS
def sqrt(x):
  try:
    return x ** 0.5
    except:
    print('x must be an int or float')
# CATCHING TYPERROR
def sqrt(x):
  try:
    return x ** 0.5
  except TypeError:
    print('x must be an int or float')
# RAISING ERROR
def sqrt(x):
  if x<0:
    raise ValueError('x must be non-negative')
  try:
    return x ** 0.5
  except TypeError:
    print('x must be an int or float')
# EXERCISE
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Initialize empty strings: echo_word, shout_words
    echo_word= ''
    shout_words=''
    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1*echo
        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word+'!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")
    # Return shout_words
    return shout_words
# Call shout_echo
shout_echo("particle", echo="accelerator")
# EXERCISE
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Raise an error with raise
    if echo<0:
         raise ValueError('echo must be greater than or equal to 0')
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # Return shout_word
    return shout_word
# Call shout_echo
shout_echo("particle", echo=5)
#EXERCISE
# Select retweets from the Twitter DataFrame: result
result = filter(lambda x:x[0:2]=='RT', tweets_df['text']) # lambda function should check if the first 2 characters in a tweet x are 'RT
# Create list from filter object result: res_list
res_list=list(result)
# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
# EXERCISE
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Add try block
    try: #TRY BLOCK: function is called with the correct arguments, it processes the DataFrame and returns a dictionary
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
    # Add except block
    except:  #except block so that when the function is called incorrectly, it displays error message:
        print('The DataFrame does not have a '+ col_name+ 'column')
# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')
# Print result1
print(result1)
#EXERCISE
# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:  #col_name is not a column in the DataFrame df, raise a ValueError
        raise ValueError('The DataFrame does not have a ' + col_name+ ' column.' )
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
result1= count_entries(tweets_df, 'lang')  # Call your new function count_entries() to analyze the 'lang' column of tweets_df
# Print result1
print(result1)










