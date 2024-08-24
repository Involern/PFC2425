# length = float(input("Enter a length: "))
# width = float(input("Enter a width: "))
# area = length * width

# print(f"The area is: {area}cm²")

# Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")