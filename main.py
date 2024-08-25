# Python temperature converter

unit = input("Is this temp. in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp / 5 + 32), 1)
    unit = 'Fahrenheit'
    print(f"The temperature in {unit} is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    unit = 'Celsius'
    print(f"The temperature in {unit} is: {temp}°C")
else:
    print(f"{unit} is invalid unit of measurement")