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


