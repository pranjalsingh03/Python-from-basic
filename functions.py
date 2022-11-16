## Functions

'''So far we have seen many built-in Python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, let us learn what a function is and why we need them?'''

### Defining a Function

'''A function is a reusable block of code or programming statements 
designed to perform a certain task. To define or declare a function, 
Python provides the _def_ keyword. The following is the syntax for 
defining a function. The function block of code is executed only if 
the function is called or invoked.'''

### Declaring and Calling a Function

'''When we make a function, we call it declaring a function. When 
we start using the it,  we call it *calling* or *invoking* a function. 
Function can be declared with or without parameters.'''

# syntax
# Declaring a function
def function_name():

# Calling a function
    function_name()

### Function without Parameters

'''Function can be declared without parameters.'''

#Example:

def generate_full_name ():
    first_name = 'Pranjal'
    last_name = 'Singh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name ()                 # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

### Function Returning a Value - Part 1

'''Function can also return values, 
if a function does not have a return statement, the value of 
the function is None. Let us rewrite the above functions using 
return. From now on, we get a value from a function when we call 
the function and print it.'''


def generate_full_name ():
    first_name = 'Pranjal'
    last_name = 'Singh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
