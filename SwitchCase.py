class Suraj:

    def calculate(self):
        while True:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))

                print("\nEnter what to do\n+ --> ADD\n- --> SUBTRACT\n* --> MULTIPLY\n/ --> DIVISION\n** --> EXPONENTIAL\n// --> FLOOR DIVISION\n") 

                c = str(input("Enter operation to do: "))

                match c:
                    case "+":
                        print(a + b)
                        print("ADD: ",(a + b))
                    case "-":
                        print(a - b)
                        print("SUBTRACT: ",(a - b))
                    case "*":
                        print(a * b)
                        print("MULTIPLY: ",(a * b))
                    case "/":
                        print(a / b)
                        print("DIVIDE: ",(a / b))
                    case "**":
                        print(a ** b)
                        print("EXPONENTIAL: ",(a ** b))
                    case "//":
                        print(a // b)
                        print("FLOOR DIVISION: ",(a // b))

                break

            except Exception as e:
                print(e)


a = Suraj()
a.calculate()