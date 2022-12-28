# List Comprehension

'''List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the _for_ loop.'''

#Example:1

'''For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:'''


# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']