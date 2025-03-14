#Day-48
#globl and local variable

x=10

def myfunc():
    y=20
    print("Local y : ",y)

    global x
    x=20
    print("Global x : ",x)

myfunc()
print(" x : ",x)