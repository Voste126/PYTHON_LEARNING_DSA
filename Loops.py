by_two = [2, 4, 6, 8, 10]

for number in by_two:
    print(number * 2)

for number in by_two:
    print("{} times 2 equals: {}.".format(number, number*2))

names = ["Tim", "Kim", "Bill", "Jill"]

for name in names:
    print("Hello {}".format(name))


# Looping using the range() function
# The range() function in Python generates a list of numbers. This list can then be looped through, as above.

# Providing a single number to range() will generate that many numbers, starting from 0 and excluding that number:
for num in range(10):
    print(num)

# Remember, in Python, the end of the range() is excluded.
# So the value 5 will not be included in the generated values.

for num in range(1, 5):
    print(num)


# List comprehensions¶
# A list comprehension is a list that is created based upon an existing list. You loop through the existing list and, optionally, perform some operation on each successive value before adding that value to the new list:
first_list = [10, 20, 30, 40]

# List comprehension (construction) based upon the elements in first_list
new_list = [item*2 for item in first_list]

print(new_list)

# Tuples
# Sometimes you’ll want to create a list of items that cannot be changed. Tuples allow you to do just that. Python refers to values that cannot be changed as immutable. A tuple is identical to a list except it is immutable.
#  A tuple is immutable, attempting to modify a tuple will result in an error message.
