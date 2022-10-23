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
