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














