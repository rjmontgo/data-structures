import math

# param str: string
# return type: string
def reverse(str):
    strl = list(str)

    temp = ''
    for i in range(math.floor(len(strl) / 2)):
        temp = strl[i]
        strl[i] = strl[len(strl) - i - 1]
        strl[len(strl) - i - 1] = temp

    return ''.join(strl)

# Simplest problem to solve
# IN - '' or 'a'
# OUT - '' or 'a'

# problem V2
# IN - 'ab'
# OUT - 'ba'

# problem V3
# IN - 'abc'
# OUT - 'cba'

# problem V4
# IN - 'abcd'
# OUT - 'dcba'



# Pattern
# moving from left to right swap each char with its mirrored index
# stop when you reach n/2 because then you will swap all chars back


# Notes/edge cases
#
