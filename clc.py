def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def calculator():
    print("=== CLI Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("Enter calculation (e.g. 5 + 3): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            num1, operator, num2 = user_input.split()
            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operator")
                continue

            print("Result:", result)

        except ValueError:
            print("Invalid input format. Use: number operator number")


if __name__ == "__main__":
    calculator()