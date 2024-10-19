# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple key-word arguments
#           * unpacking operator
#           1. positional 2. default 3. keyword 4. ARBITRARY
# varying amount of arguments

def shipping_label(*args, **kwargs): #order for args and kwargs MATTERS
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('state')}")

shipping_label("Dr.", "Spongebob", "Squarepants", 
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")


# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 Fake St.",
#               apt="100",
#               city="Detroit", 
#               state="MI", 
#               zip="54321")

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr", "Spongebob", "Harold", "Squarepants", "III")