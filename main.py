# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable seperate files

# import math
# import math as m # as assigns an alias to reduce typing if you have a long module name.
# from math import pi
# from math import e #no longer need to use "math". Might result in name conflicts, so use sparingly.

# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), 'EXTRA'))

import example as e

result = e.pi
result = e.square(3)
result = e.cube(3)
result = e.circumference(3)
result = e.area(3)

print(result)



# a, b, c, d, e = 1, 2, 3, 4, 5 # this makes "e" from the math import no longer be used.
# # always uses second instance of "e"

# print(e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** e)