# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. Positional 2. Default 3. KEYWORD 4. Arbitrary

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)

# print("1", "2", "3", "4", "5", sep="-") #keyword argument is "sep"



# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello(first="Spongebob", greeting="Hello", last="Squarepants", title="Mr.") #doesn't matter position of the arugments.


# for x in range(1, 11):
#     print(x, end=" ") #end is a keyword argument in print.