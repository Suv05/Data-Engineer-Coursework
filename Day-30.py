#video 57

class Details:
    name = "Harry"
    job = "SWE"

    def info(self):
        print(f"{self.name} is a {self.job}")


# Create an object and call the method
a = Details()
a.job = "cleaner"
a.name = "suv"
a.info()
