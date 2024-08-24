import time
t = time

while True:
    USER = input("Please enter your Username: ")
    if bool(USER):
        print(f"Great! Your name is {USER}")
        break
    else:
        print("Invalid")
        t.sleep(0.5)