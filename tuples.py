## Day06 - Tuples

'''A tuple is a collection of different data types which is ordered and unchangeable (immutable). 
Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. 
We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). 
Unlike list, tuple has few methods. Methods related to tuples:

- tuple(): to create an empty tuple
- count(): to count the number of a specified item in a tuple
- index(): to find the index of a specified item in a tuple
- + operator: to join two or more tuples and to create a new tuple'''

# Empty tuple: Creating an empty tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

#Tuple with initial values
  
# syntax
tpl = ('item1', 'item2','item3')

fruits = ('banana', 'orange', 'mango', 'lemon')

### Tuple length

#We use the _len()_ method to get the length of a tuple.

# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)

### Accessing Tuple Items

# Positive Indexing
# Similar to the list data type we use positive or negative indexing to access tuple items.


# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]


fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

# Negative indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list/tuple length refers to the first item.

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

### Changing Tuples to Lists

# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')