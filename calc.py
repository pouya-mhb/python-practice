input1 = float(input("Enter a number: "))
input2 = float(input("Enter a number: "))
numbers = []
numbers.append(input1)
numbers.append(input2)

oprand = input("Enter an operation (+, -, *, /): ")

if oprand == "+":
    result = input1 + input2
elif oprand == "-":
    result = input1 - input2
elif oprand == "*":
    result = 1
    result = input1 * input2
elif oprand == "/":
    if input2 != 0:
        result = input1 / input2
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")

if result is not None:
    print("Result:", result)
else:
    print("Error: Invalid operation.")


while True:
    input3 = float(input("Enter a number: "))
    oprand = input("Enter an operation (+, -, *, /): ")

    if oprand == "+":
        result = result + input3
    elif oprand == "-":
        result = result - input3
    elif oprand == "*":
        result = result * input3
    elif oprand == "/":
        if input3 != 0:
            result = result / input3
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation.")

    print("Result:", result)
