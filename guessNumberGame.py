import random

computer_number = random.randrange(0, 100)
print(f"computer number : {computer_number}")


def guess_number():
    user_number = int(input("Enter your number : "))
    return user_number


def game(guess, computer_number):
    if guess < computer_number:
        return "Too low"
    elif guess > computer_number:
        return "Too high"
    else:
        return "Correct"


guess = 0

while guess != computer_number:
    guess = guess_number()
    result = game(guess, computer_number)
    print(guess)
    print(result)
