class Animal:
    def __init__(self):
        print("Animal Created")
        # this method returns None when there is no params

    def who_is_this(self):
        print("This is an animal")

    def eat(self):
        print("The animal is eating.")


the_animal = Animal()

print(the_animal.who_is_this())


# Let's inherit from Animal Class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)  # init from mother class
        print("Dog Created")

    def bark(self):
        print("Woof !")

    # Override the inherited method
    def who_is_this(self):
        print("This is a dog !")


my_dog = Dog()
my_dog.eat()
my_dog.bark()
my_dog.who_is_this()
