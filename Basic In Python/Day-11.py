# video-22 List
from tkinter.font import names

a = [1, 5, "harry", True]
print(a[0])
print(a[2])
print(a[1])
print(a[-1])
print(len(a))

b = ["suv", "you", "mu", "ankita", "ramu"]
b[4] = "sita"
print(b)
print(b[1:-1:2])
print(b[1:-1])

if "me" in b:
    print(True)

namesWith_u = [item for item in b if "u" in item]
print(namesWith_u)

# list comprehension
lst = [i * i for i in range(10)]
print(lst)
lst1 = [i * i for i in range(10) if i % 2 == 0]
print(lst1)
