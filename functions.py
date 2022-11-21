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

### Function with Parameters

'''In a function we can pass different data types(number, string, 
boolean, list, tuple, dictionary or set) as a parameter'''

#- Single Parameter: If our function takes a parameter we should call our function with an argument


# syntax
# Declaring a function
def function_name(parameter):
#    codes
#   codes
# Calling function
    print(function_name(argument))


#Example:

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Pranjal'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
'''Two Parameter: A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments. Let us check a function with two parameters:'''

# syntax
# Declaring a function
def function_name(para1, para2):
#   codes
#   codes
# Calling function
    print(function_name(arg1, arg2))



#Example:

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Pranjal','Singh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N'               # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

### Passing Arguments with Key and Value

'''If we pass the arguments with key and value, the order of the arguments does not matter.'''

# syntax
# Declaring a function
def function_name(para1, para2):
#    codes
#   codes
# Calling function
    print(function_name(para1 = 'Magan', para2 = 'Pranjal')) # the order of arguments does not matter here

#Example:


def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Pranjal', lastname = 'Singh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2))      # Order does not matter

### Function Returning a Value - Part 2

'''If we do not return a value with a function, then our function is returning _None_ by default. To return a value with a function we use the keyword _return_ followed by the variable we are returning. We can return any kind of data types from a function.'''

# Returning a string:
#Example:

def print_name(firstname):
    return firstname
print_name('Pranjal') # Pranjal

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Pranjal', lastname='Singh')

#Returning a number:

#Example:

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))

#Returning a boolean:

#Example:

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True     # return stops further execution of the function, similar to break 
    return False
print(is_even(10))      # True
print(is_even(7))       # False


#Returning a list:
#Example:

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
