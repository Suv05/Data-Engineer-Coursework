# match case

n = int(input("Enter a number: "))

match n:
    case 0:
        print("x is 0")
    case 2:
        print("x is 2")
    case _ if n == 20:
        print(n,"equal")
    case _ if n != 14:
        print(n,"equal not")
    case _:
        print(n)
