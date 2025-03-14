# video-59
#decorator in python

def logging(fx):
    def wrapper(*args, **kwargs):  # This function wraps around the original function
        print("Thanks for logging")
        return fx(*args, **kwargs)  # Call the original function with arguments
    return wrapper  # Return the wrapper function


@logging
def func(name, password):
    print(f"{name} of this {password}")


# Calling the function
func("Harry", "#123")
