"""
Dictionary
A dictionary is a collection which is unordered,
changeable and indexed. In Python dictionaries 
are written with curly brackets, and they have 
keys and values.
"""

dictionary =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dictionary["model"])
dictionary.popitem()
dictionary.__iter__:8

for x, y in dictionary.items():
  print(x, ":",y)

if "model" in dictionary:
  print("Yes, 'model' is one of ",
   "the keys in the thisdict dictionary")

"""
Using dict() constructor
"""
thisdict = dict(brand="Ford", model="Mustang", year=1964)

""""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing the a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""