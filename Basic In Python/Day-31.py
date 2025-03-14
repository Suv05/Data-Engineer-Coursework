# video 58

class Details:

    def __init__(self, name, occ):
        self.name = name
        self.job = occ

    def info(self):
        print(f"{self.name} is a {self.job}")


a = Details("gary", "swe")
a.info()

b = Details("divya", "cleaner")
b.info()
