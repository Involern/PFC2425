import time as t

# # Collection
# # Tuples. Ordered and unchangeable. Duplicates OK. FASTER


# fruits = ('apple', 'orange', 'banana', 'coconut', 'coconut')
# # print(dir(fruits))
# print(help(fruits))

# print(fruits)


multiplier_map = {
    -6: .25,
    -5: .29,
    -4: .33,
    -3: .4,
    -2: .5,
    -1: .67,
    0: 0,
    1: 1.5,
    2: 2,
    3: 2.5,
    4: 3,
    5: 3.5,
    6: 4
}

base = 52
stage = 8
mult = multiplier_map.get(stage, -6 if stage <= -6 else (6 if stage >= 6 else stage))

# print('Too high or low stage!' if mult >= -6 or mult <= 6 else '')

def multiplierBase(baset):
    newVal = baset * (1 if stage == 0 else mult)
    print(f"base is {baset} and multiplier is {mult}")
    if stage in [-5, -4, -1]:
        round(newVal, 2)
    return newVal

print(f'Final stat {multiplierBase(base)}')

t.sleep(2)
print('slept!')