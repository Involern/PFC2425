import random

low = 1
high = 100
options = ("rock", "paper", "scissors")

# number = random.randint(low, high)
# number = random.random() # random float from 0 to 1
# option = random.choice(options)
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)

print(cards)