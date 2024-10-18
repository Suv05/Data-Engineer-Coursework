# video 52 lamda functions
add = lambda x, y: x + y
print(add(1, 2))
square = lambda x: x * x
print(square(4))


# pass function as an argument
def app(fx, value):
    return 6 + fx(value)


print(app(square, 4))
