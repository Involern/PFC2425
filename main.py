# nested loop

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symnol to use: ")


for x in range (rows):
    for y in range(columns):
        print(symbol, end="")
    print()