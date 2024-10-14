# factorial calculation
def factorial(num):
    if num == 1 or num == 0:
        return num
    else:
        return num * factorial(num - 1)


print(factorial(3))


# fibbonaci series calculation
def fibbonaci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    elif index == 2:
        return 2
    else:
        return index - 1 + fibbonaci(index - 2)


print(fibbonaci(5))
