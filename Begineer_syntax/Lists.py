thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

#insert a item
thislist.insert(1, "orange")
print(thislist)

#extend a list
thislist.extend(tropical)
print(thislist)
#Remove the item from the list
thislist.remove("banana")
print(thislist)