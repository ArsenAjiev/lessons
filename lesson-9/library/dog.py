class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def change_name(self, name):
        self.name = name

    def jump(self):
        print(f"{self.name} is jumped")

    def run(self):
        print(f"{self.name} is running")

    def bark(self):
        print(f"{self.name} is barking")