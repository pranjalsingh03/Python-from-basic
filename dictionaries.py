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
