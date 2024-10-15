# short=hand if else video-41 & 42

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("hello") if a > b else print("hii")

# enumerator function
marks = [1, 8, 9, 6, 0, 7, 5, 6, ]

for idx, mark in enumerate(marks, start=1):
    print(idx, mark)
    if idx == 3:
        print("Found it")
