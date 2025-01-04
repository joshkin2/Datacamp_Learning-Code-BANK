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
