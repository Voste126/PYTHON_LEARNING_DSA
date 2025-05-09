# Conditional tests
# At the heart of every if statement is an expression that can be evaluated as True or False (Booleans) and is called a conditional test. Python uses the values True and False to decide whether the code in an if statement should be executed. If a conditional test evaluates to True, Python executes the indented code block following the if statement. If the test evaluates to False, Python ignores the code following the if statement.


# if <condition>:
#     block of code
#     blocks begin and end with indentation, traditionally 4 spaces

#     if <condition>:
#         block of code
#         this is another if statement

user_email = "jeff@amazon.com"
password = "bezos"

if user_email == "jeff@amazon.com":
    if password == "bezos":
        print("Access granted.")


names = ["Tim", "Kim", "Bill", "Jill"]

for name in names:
    if len(name) == 3:
        print(f"Hey three-letter {name}")

#check if a value is in a list
names = ["Tim", "Kim", "Bill", "Jill"]

"Kim" in names


age = 25

if age < 10:
    print("Just a kid.")
elif age < 16:
    print("Can't drive yet!")
elif age < 21:
    print("No drinking for you!")
else:
    print("You're good to go!")


names_list = ["Angela", "Vince", "Andy", "Mike"]

[name for name in names_list if name not in ["Andy", "Mike"]]

test_scores = [73, 92, 81, 62, 58, 89]

[print("Pass") if score > 75 else print("Fail") for score in test_scores]