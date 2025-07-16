print("Arithmetic Calculator for 2 Numbers\n\nUse the following arithmetic operators:\n/  : Division\n-  : Subtraction+  : Addition\n*  : Multiplication\n// : Integer (approximate) quotient\n%  : Remainder\n^  : Exponentiation\n")
while True:
    try:
        a = int(input("Enter first number: "))
        c = input("Enter an arithmetic operator: ")
        
        if c not in ["+", "-", "*", "/", "//", "%", "^"]:
            print("Invalid operator! Use only +, -, *, /, //, %, ^ .Restarting...")
            continue

        b = int(input("Enter second number: "))

        print("Result:")
        if c == "+":
            print(f"{a} + {b} = {a + b}")
        elif c == "-":
            print(f"{a} - {b} = {a - b}")
        elif c == "*":
            print(f"{a} * {b} = {a * b}")
        elif c == "/":
            if b == 0:
                print("Division by zero not allowed!")
            else:
                print(f"{a} / {b} = {a / b}")
                print(f"Integer quotient: {a // b}")
                print(f"Remainder: {a % b}")
        elif c == "//":
            if b == 0:
                print("Division by zero not allowed!")
            else:
                print(f"{a} // {b} = {a // b}")
        elif c == "%":
            if b == 0:
                print("Division by zero not allowed!")
            else:
                print(f"{a} % {b} = {a % b}")
        elif c == "^":
            print(f"{a} ^ {b} = {a ** b}")
        
        print("Do you want to perform another operation?\n1 for YES\n2 for NO")
        choice = input("Enter choice: ")

        if choice == "2":
            print("THANK YOU for using the calculator!")
            break
        elif choice != "1":
            print("Invalid choice. Exiting...")
            break

    except ValueError:
     print("Please enter valid integer numbers only.")