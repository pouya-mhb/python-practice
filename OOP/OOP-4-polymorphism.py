# Polymorphism
# refes the way in which different object classes can share the same method name
# and thos methods can be called the same place from diffrerent objects passed in


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(
        self,
    ):  # here the speakl method is the same method in both cat and dog classes
        return self.name + "says woof !"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says meow !"


nikki = Dog(name="nikki")
filix = Cat(name="filix")

print(nikki.speak())
print(filix.speak())

for pet in [nikki, filix]:
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(nikki)
pet_speak(filix)
