# Dictionaries
# A dictionary in Python is a collection of key-value pairs. We can access data using a key rather than using its index position as we do with lists.

# Each key, in a dictionary, is associated with a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.

# In Python, a dictionary is wrapped in curly braces {}, with a series of key-value pairs inside the braces. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas. You can store as many key-value pairs as you desire in a dictionary.

person = {"Name": "Alan Mills", "Age": 47, "Children": ["Carrie", "Sara", "Ben"]}
print(person)
print(person["Name"])
print(person["Age"])

#Adding data (key-value pairs) to a dictionary
person["Occupation"] = "Software Engineer"
print(person)

# Modifying values in a dictionary
person["Occupation"] = "Senior Software Engineer"
print(person)

person["Children"][2] = "Benjamin"
print(person)

#Removing key-value pairs from a dictionary
del person["Age"]
print(person)


#Create a dictionary associating each month of the year with the number the month is within the year (e.g., January's value would be 1, July's value would be 7).

# Access your dictionary to print December's value
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
print(months["December"])

#Looping through the key-value pairs in a dictionary

person = {"Name": "Alan Mills", "Children": ["Carrie", "Sara", "Ben"]}

for key, value in person.items():
    print(key)
    print(value)

# The method items() returns a tuple containing a key-value pair. 
# The tuple can be unpacked (assigned to individual variables) by giving the for loop two variables, as above.

for key_value_pair in person.items():
    print(key_value_pair)


### Looping through all of the keys in a dictionary
for key in person:
    print(key)

# Same result as above
for key in person.keys():
    print(key)

#looping through all of the values in a dictionary

for value in person.values():
    print(value)
