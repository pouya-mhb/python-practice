
class Factorial:
    def __init__(self, number):
        self.number = number

    def calculate_factorial (self):
        result = 1
        for i in range (self.number):
            result = result * self.number
            self.number = self.number - 1
        return result

# factorial = Factorial(5)

# print(factorial.calculate_factorial())