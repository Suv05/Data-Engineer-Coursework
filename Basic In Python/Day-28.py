# map filter reduce

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# newLi = map(lambda x: x + 2, li)

# newLi=filter(lambda x:x>5,li)

from functools import reduce

newLi = reduce(lambda x, y: x + y, li)
print(newLi)
