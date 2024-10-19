# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

email = "spongebob@gmail.com"

if "@" in email and "." in email: # checking two conditions of two values that is found in the sequence "email"
    print("Valid email")
else:
    print("Invalid email")






# grades = {"Sandy": "A", 
#           "Squidward": "B", 
#           "Spongebob": "C", 
#           "Patrick": "D"}

# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")







# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of a student: ")

# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")






# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter not in word: # in checks if letters or something was found in sequence and then returns boolean
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")