class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self} created")

    def __del__(self):
        print(f"{self} deleted")

    def __str__(self):
        return f"Animal(name='{self.name}',age='{self.age}')"


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"Dog(name='{self.name}',age='{self.age}')"

    def speak(self):
        return f"{self.name} says: Woof!"


class Shelter:
    animals = []

    def __init__(self, init_animals = None):
        if init_animals is not None:
            self.animals += init_animals

    def __len__(self):
        return len(self.animals)

    def __str__(self):
        return "\n".join(str(a) for a in self.animals)

    def add_animal(self, animal):
        self.animals.append(animal)

shelter = Shelter()
shelter.add_animal(Dog("Spiky", 5))
shelter.add_animal(Animal("Meowt", 4))
print(shelter)

