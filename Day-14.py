# video-25 tuple methods
tup = (1, 7, 8, 9, 9, 5)
l1 = list(tup)
l1.append("hello")
tup = tuple(l1)
print(tup)


print(tup.count(9))
print(tup.index(9))