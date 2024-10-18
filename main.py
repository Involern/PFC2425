# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

items = capitals.items()
for key, value in capitals.items():
    print(f"Key: {key}, \nValue: {value}", end=",\n\n")

# values = capitals.values()
# for value in capitals.values():
#     print(value)


# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# while True:
#     getCap = input("What country?: ").upper()
#     if capitals.get(getCap):
#         print(capitals[getCap])
#     elif getCap.upper() == "Q":
#         break
#     else:
#         print("That capital doesn't exist")