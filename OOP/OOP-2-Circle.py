class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_circumfrence(self):
        return self.radius * self.pi * 2

    def get_area(self):
        return self.pi * self.radius**2


the_circle = Circle(radius=3)

print(the_circle.pi)
print(the_circle.radius)
print(the_circle.get_area())
print(the_circle.get_circumfrence())
