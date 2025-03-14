# inheritance in python video-61

class Employee:

    def __init__(self, name, ids):
        self.name = name
        self.id = ids

    def showDetails(self):
        print(f"Name: {self.name} and ID: {self.id}")


class Developer(Employee):
    def __init__(self, name, ids, language):
        super().__init__(name, ids)
        self.language = language

        print(f"Name: {self.name} and ID: {self.id} and Language: {self.language}")


a = Developer("Harry",123,"Hindi")
a.showDetails()
