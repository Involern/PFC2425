# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")


# name = "Spongebob Squarepants"

# for character in name:
#     print(character, end=" ")


# fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in reversed(fruits): # you cannot reverse sets.
#     print(fruit)

# numbers = (1, 2, 3, 4, 5)

# for number in numbers: #variable should be in relation to iterable for readability
#     print(number)