# A set is a data structure that can only contain unique elements. A set can formally be created using curly braces and ensures that each item within it is unique. The elements are returned in alphabetical order.
# A set is unordered so it can't be accessed using indexing.

{"Stanford", "USC", "UCLA", "UCLA", "Stanford", "USC", "Berkeley", "Berkeley"}

a_list = [15, 100, 15, 10, 15, 15, 10, 5, 100, 5, 15, 15, 10, 5, 100, 5, 15, 100, 15, 10, 15, 15, 10, 5]

a_set = set(a_list)

print(a_set)
