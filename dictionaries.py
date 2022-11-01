# 📘 Day 8

## Dictionaries

#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

### Creating a Dictionary

#To create a dictionary we use curly brackets, {} or the *dict()* built-in function.

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


#Example:

person = {
    'first_name':'Pranjal',
    'last_name':'Singh',
    'age':18,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'CSS', 'HTML', 'Python'],
    'address':{
        'street':'Gorakhpur',
        'zipcode':'274207'
    }
    }

#The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.

### Dictionary Length

#It checks the number of 'key: value' pairs in the dictionary.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct))            # 4

#Example:

person = {
    'first_name':'Pranjal',
    'last_name':'Singh',
    'age':18,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'CSS', 'HTML', 'Python'],
    'address':{
        'street':'Gorakhpur',
        'zipcode':'274207'
    }
    }
print(len(person))     # 7

### Accessing Dictionary Items

#We can access Dictionary items by referring to its key name.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4

#Example:

person = {
    'first_name':'Pranjal',
    'last_name':'Singh',
    'age':18,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'CSS', 'HTML', 'Python'],
    'address':{
        'street':'Gorakhpur',
        'zipcode':'274207'
    }
    }

print(person['first_name']) # Pranjal 
print(person['country'])    # India
print(person['skills'])     # ['JavaScript', 'React', 'CSS', 'HTML', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Gorakhpur 
print(person['city'])       # Error

#Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the _get_ method. The get method returns None, which is a NoneType object data type, if the key does not exist.

person = {
    'first_name':'Pranjal',
    'last_name':'Singh',
    'age':18,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'CSS', 'HTML', 'Python'],
    'address':{
        'street':'Gorakhpur',
        'zipcode':'274207'
    }
    }
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

### Adding Items to a Dictionary

#We can add new key and value pairs to a dictionary


# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'


#Example:
person = {
    'first_name':'Pranjal',
    'last_name':'Singh',
    'age':18,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'CSS', 'HTML', 'Python'],
    'address':{
        'street':'Gorakhpur',
        'zipcode':'274207'
    }
    }

### Modifying Items in a Dictionary

#We can modify items in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

#Example:

person = {
    'first_name':'Pranjal',
    'last_name':'Singh',
    'age':18,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'CSS', 'HTML', 'Python'],
    'address':{
        'street':'Gorakhpur',
        'zipcode':'274207'
    }
    }
person['first_name'] = 'Eyob'
person['age'] = 252

### Checking Keys in a Dictionary

#We use the _in_ operator to check if a key exist in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

### Removing Key and Value Pairs from a Dictionary

#_pop(key)_: removes the item with the specified key name:
#_popitem()_: removes the last item
#_del_: removes an item with specified key name

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item


#Example:

person = {
    'first_name':'Pranjal',
    'last_name':'Singh',
    'age':18,
    'country':'India',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'CSS', 'HTML', 'Python'],
    'address':{
        'street':'Gorakhpur',
        'zipcode':'274207'
    }
    }
