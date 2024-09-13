# collection = single "variable" used to store multiple values
# list: order and changeable. Duplicate ok
# Set: unordered and immutable, but Add/Remvoe OK. No duplicates
# Tuple: () ordered and unchangeable. Duplicates ok. Faster

fruits = ("apple", "orange", "banana", "coconut", "apple", "apple")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits[0]) # cannot use indexing on set because it is unordered

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("apple"))

for fruit in fruits:
    print(fruit)

print(fruits)