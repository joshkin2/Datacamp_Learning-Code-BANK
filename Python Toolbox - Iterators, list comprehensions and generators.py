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
