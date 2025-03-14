#video-37 & 38
try:
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
finally:
    print("i am always runed")

print("Some important lines of code")

#throw custom error
a=6
if a>5 or a<9:
    raise Exception("Division by zero is not possible")

