n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operator = input("Enter operator: ")

if operator == "+":
    print("SUM: ", n1 + n2)

elif operator == "-":
    print("Subtraction: ", n1 - n2)

elif operator == "*":
    print("Multiplication: ", n1 * n2)

elif operator == "/":
    print("Division: ", n1 / n2)

elif operator == "//":
    print("Floor division: ", n1 // n2)

elif operator == "**":
    print("Power of: ", n1 ** n2)

elif operator == "%":
    print("Modulo: ", n1 % n2)

else:
    print("Invalid operation")

