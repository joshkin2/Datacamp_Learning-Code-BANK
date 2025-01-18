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

