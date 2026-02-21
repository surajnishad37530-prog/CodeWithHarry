a = 34
b = 56
c = 98

"""
print the sum of three these three numbers
Biggest among these three numbers
smallest among these three numbers
"""
# d = (a+b+c)
# print(d)

print(f"The sum of the these three numbers is {a+b+c}\n")

if b < a > c:
    print(f"The biggest number is {a}")
elif a < b > c:
    print(f"The biggest number is {b}")
else:
    print(f"The biggest number is {c}")

if b > a < c:
    print(f"The smallest number is {a}")
elif a > b < c:
    print(f"The smallest number is {b}")
else:
    print(f"The smallest number is {c}")