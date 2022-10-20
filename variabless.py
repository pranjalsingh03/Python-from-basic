#Day02 - Variables in Python

#Started my Day02 of learning Python with variables

first_name = 'Pranjal'
last_name = 'Singh'
country = 'India'
city = 'Gorakhpur'
age = 18
skills = ['HTML', 'CSS', 'Python']
person_info = {
    'firstname':'Pranjal', 
    'lastname':'Singh', 
    'country':'India',
    'city':'Gorakhpur'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))     #To print length of the sentense
print('Last name: ', last_name)                  
print('Last name length: ', len(last_name))      #To print length of the sentense
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line using Single command line

first_name, last_name, country, age = 'Pranjal', 'Singh', 'India', 18

print(first_name, last_name, country, age)             #To print to complete sentense in one line
print('First name:', first_name)                       #First_name=Pranjal
print('Last name: ', last_name)                        #Last_name=singh
print('Country: ', country)                            #Country=India
print('Age: ', age)                                    #Age=18