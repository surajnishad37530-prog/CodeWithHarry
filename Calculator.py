class Calculator:

    def calculate(self):
        while True:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))

                print("\nEnter what to do\n1 --> Add\n2 --> Subtract\n3 --> Multiply\n4 --> Divide\n5 --> Exponential\n6 --> Floor Division\n7 --> To do all operations simultaneously\n")

                c = int(input("Enter operation to do: "))
                print("\n")
                
                if c == 1:
                    print(a + b)
                    print(f"The addition of {a} and {b} is {a + b}")
                elif c == 2:
                    print(a - b)
                    print(f"The subtraction of {a} and {b} is {a - b}")
                elif c == 3:
                    print(a * b)
                    print(f"The multiplication of {a} and {b} is {a * b}")
                elif c == 4:
                    print(a / b if b != 0 else "Error: Division by zero")
                    print(f"The division of {a} and {b} is {a / b}")
                elif c == 5:
                    print(a ** b)
                    print(f"The Exponential of {a} and {b} is {a ** b}")
                elif c == 6:
                    print(a // b)
                    print(f"The Floor Division of {a} and {b} is {a // b}")
                elif c == 7:
                    print(f"Add: {a + b}\nSubtract: {a - b}\nMultiply: {a * b}\nDivide:{a / b}\nExponential: {a ** b}\nFloor Division: {a // b}")

                break

            except Exception as e:
                print(e)

        

a = Calculator()
a.calculate()