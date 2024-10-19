# # function = A block of reusable code
# #           place () after the function name to invoke it

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)






# def happy_birthday(name, age):
#     print(f'Happy Birthday to {name}!')
#     print(f'You are {age}!')
#     print(f'Happy Birthday to {name}!')
#     print()

# happy_birthday("Name", 20)
# happy_birthday("Joe", 45)
# happy_birthday("Sarah", 425)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Username", 24.123219, "01/01")
# print()
# display_invoice("2guy", 101.0111111111, "01/23")

# def add(x, y):
#     z = x + y
#     return z

# def sub(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(sub(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))