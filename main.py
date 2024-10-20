# variable scope = where a variable is visible and accesible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

from math import e # built in version of e via math module

def func1():
    print(e)

# e = 3 # global version of e

func1()

# def func1():
#     print(x)

# def func2():
#     print(x)

# x = 3

# func1()
# func2()