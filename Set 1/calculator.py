def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    elif operator == "%":
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 % num2
    else:
        return "Invalid operator given."


def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter your operator: ")

    result = calculator(num1, num2, operator)

    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
