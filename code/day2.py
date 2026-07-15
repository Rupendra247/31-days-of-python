
"""
Day 2: Data Types
- Python uses dynamic typing (no need to declare int/string).
- Use type() to inspect data types.
"""

# Basic types
age = 25              # int
price = 19.99         # float
name = "Alice"        # str
is_student = True     # bool

# Type casting: Converting data types
# Useful for input processing where everything is a string initially
age_as_str = str(age)
print(f"Age as string: {age_as_str}, Type: {type(age_as_str)}")

# Math with different types
total = age + int(price) # Converting float to int truncates the decimal
print(f"Total: {total}")

# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
