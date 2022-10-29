## Day07- Sets

# Hello everyone we have sucessfuly completed our journey till tuples and we are starting with sets

## Sets

'''Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the _union_, _intersection_, _difference_, _symmetric difference_, _subset_, _super set_ and _disjoint set_ among sets.'''

### Creating a Set

#We use curly brackets, {} to create a set or the *set()* built-in function.

#Creating an empty set

# syntax
st = {}

# or

st = set()


#Creating a set with initial items

# syntax
st = {'item1', 'item2', 'item3', 'item4'}

#Example:

# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}

### Getting Set's Length

#We use **len()** method to find the length of a set.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(set)

#Example:

fruits = {'banana', 'orange', 'mango', 'lemon', 'strawberry'}
len(fruits)

### Accessing Items in a Set

# We use loops to access items. We will see this in loop section

### Checking an Item

# To check if an item exist in a list we use _in_ membership operator.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st)         # Does set st contain item3? True

#Example:


fruits = {'banana', 'orange', 'mango', 'lemon', 'strawberry'}
print('mango' in fruits )       # True

### Adding Items to a Set

# Once a set is created we cannot change any items and we can also add additional items.

# Add one item using _add()_

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

#Example:

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

#Add multiple items using _update()_
# The *update()* allows to add multiple items to a set. The *update()* takes a list argument.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

#Example:

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)


### Removing Items from a Set

#We can remove an item from a set using _remove()_ method. If the item is not found _remove()_ method will raise errors, so it is good to check if the item exist in the given set. However, _discard()_ method doesn't raise any errors.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')


#The pop() methods remove a random item from a list and it returns the removed item.

#Example:

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set



#If we are interested in the removed item.

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 



### Clearing Items in a Set

#If we want to clear or empty the set we use _clear_ method.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

#Example:

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

### Deleting a Set

#If we want to delete the set itself we use _del_ operator.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st

#Example:

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

### Converting List to Set

#We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.

# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

#Example:

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

### Joining Sets

#We can join two sets using the _union()_ or _update()_ method.

#Union
#This method returns a new set

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

#Example:

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Update
# This method inserts a set into a given set

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1


# **Example:**

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}


### Finding Intersection Items

# Intersection returns a set of items which are in both the sets. See the example

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}


# **Example:**

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}


### Checking Subset and Super Set

#A set can be a subset or super set of other sets:

# Subset: _issubset()_
# Super set: _issuperset_

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True


# **Example:**

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)           # False, because it is a super set
whole_numbers.issuperset(even_numbers)         # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False


### Checking the Difference Between Two Sets

# It returns the difference between two sets.

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2


# Example:

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}


### Finding Symmetric Difference Between Two Sets

# It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1)                    # {'item1', 'item4'}


# Example:

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)             # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}


### Joining Sets

# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using _isdisjoint()_ method.

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1)                      # False


# Example:

even_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(even_numbers)    # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)               # False, there are common items {'o', 'n'}



