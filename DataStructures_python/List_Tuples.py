# A second colon (:) can be used to indicate step size. list[start:stop:stepsize]

states = ["CA", "FL", "TX", "NY", "AZ", "HI", "OR", "NJ"]
print(states[0:5:2])

print(states[::2])    # This returns every other item in the list, from beginning to end.

print(states[::-1])   #The below code will return every item in a list, starting from the end. In other words, it returns a reversed copy of the list: