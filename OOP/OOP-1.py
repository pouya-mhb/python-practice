class Dog:
    # Class object attribute
    # Same for any instance of a class
    Species = "Mammal"  # all dogs are mammal

    def __init__(self, dog_breed, name, spots):
        # Attributes
        # we take it in argument
        # self.atttribute_name
        self.breed = dog_breed
        self.name = name

        # Expect boolean for spots
        # self.spots = True
        self.spots = spots

    # oprations / actions --> methods
    def bark(self):
        print("Woof")

    def walk(self):
        print(f"{self.name} is walking .. !")

    def hi(self, number):
        print(f" hi my name is {self.name} and the number is {number}")


my_dog = Dog(dog_breed="Labrador", name="Alex", spots="NO Spots")
print(my_dog.breed)
print(my_dog.Species)
print(my_dog.name)
print(my_dog.spots)


my_dog.bark()
my_dog.walk()
my_dog.hi(10)
