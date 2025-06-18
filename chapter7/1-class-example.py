class Dog():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return f"Dog(name='{self.name}',color='{self.color}')"

dog = Dog("Spiky", "blue")
print(dog)