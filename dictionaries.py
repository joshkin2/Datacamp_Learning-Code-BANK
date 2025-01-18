#turn dict into dataframe called cars
cars = pd.DataFrame(my_dict)

# converting lists to dictionaries
pop = [30.55, 2.77, 39.21] # list
countries = ["afghan", "albania", "algeria"] # list
world = {"afghan":30.55, "albania":2.77. "algreria":39.21} # dict
# to find value of albania in dict use
world["albania"]

#To get position of a value in a list use
new variable = variablethatcontainsvalueneeded.index("value you're looking for")
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

# Correct way to add a key-value pair to a dictionary
data = {'capital': 'rome', 'population': 59.83}
europe['italy'] = data
print(europe)

#delete key from a dict
del dict_name[key]
#to see all the keys in a dict
dict.keys()
#see all values in a dict
dict.values()
#extract keys in a dict as a list
list(dict.keys())

#print out elemenets in a dict using for loop(output may be unordered)
world = {"ghana":20,
         "usa": 2.5.
         "nigeria":23}
for key, value in world.items():
    print(key + "--" + str(value))

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





















