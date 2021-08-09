class Animal:

    def __init__(self, height, weight, name, age=10):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

    def jump(self):
        print(f"{self.name} is jumping")

    def run(self):
        print(f"{self.name} is running")