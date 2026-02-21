
a = int(input("Enter a Number to print table: "))

for i in range(1, 11):
    print(f"{a} X {i} = {a * i}")


print("\n")


def fibonacci(n):
    a, b = 0, 1

    for _ in range(1, n+1):
        print(a)
        a, b = b, a + b


fibonacci(10)


print("\n")

def factorial(n):
     
    t = 1
    for i in range(1, n+1):
        t = t * i
        
    print(t)

b = int(input("Enter a number to find factorial: "))
factorial(b)