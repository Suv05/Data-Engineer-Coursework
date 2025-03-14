# video-24 Tuples
# Tuples are immutable so to add or delete i have to first convert the Tuple to list
tup = (1, 5, 7, "suv", "wte")
print(type(tup), tup)
# tup[0] = 5  error tuple doesn't support item assignment

# one element is treated as int if not added ,
# tup1=(1,)
# print(print(type(tup1),tup1))

print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[1:-1:2])

if "suv" in tup:
    print("yes")

