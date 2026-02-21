# a = "suraj"
# print(type(a))

# a = 4353
# print(type(a))

# a = True
# print(type(a))

# a = int(input("Enter first Number: "))
# b = int(input("Enter second Number: "))

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a ** b)
# print(a // b)
# print(a % b)

# def Odd_Even():
#     while True:
#         try:
#             a = int(input("Enter a Number: "))
#             if a < 0 or a == 0:
#                 print("Please enter number greater than 0")
#                 continue   
#             elif a % 2 == 0:
#                 print("The Number is even")
#                 break
#             else:
#                 print("The Number is odd")
#                 break
#         except Exception as e:
#             print(type(e))
#             print(e)
#             continue
        


#def Odd_Even():
#    while True:
#        try:
#            a = int(input("Enter a Number: "))
#            if a < 0 or a == 0:
#                if a < 0:
#                    print("Please enter positive number")
#                elif a == 0:
#                    print("Please enter number greater than 0")
#                continue   
#            elif a % 2 == 0:
#                print("The Number is even")
#                break
#            else:
#                print("The Number is odd")
#                break
#        except Exception as e:
#            print(type(e))
#            print(e)
#            continue
#
#
# #Odd_Even()
# a=complex(4+6)
# b="suraj"
# print("the type of  a is:",type(a))


# dict1={"name":"suraj","age":20,"can vote":True}
# print(dict1)

#dict1 = {
#    "Name": "Suraj",
#    "Age": 20,
#    "Roll no.": 636,
#    "College": "Dyansadhna"
#}
#
#
## print(dict1)
#
## for key in dict1:
##     print(key)
#
## for key,value in dict1.items():
##     print(key, ":", value)
#
#list1 = ["Mango", "Apple", "Banana", 43, 345, 567, 678, True, False]
#
## print(list1)
#
## for i in list1:
##     print(i)
#
#list1.insert(2, "Suraj")
#print(list1)
#
#print(type(list1))
#
#tuple1 = ("Mango", "Apple", "Banana", 43, 345, 567, 678, True, False)
#
#print(type(tuple1))
#
#set1 = {"Mango", "Apple", "Banana", 43, 345, 567, 678, True, False}
#
#print(type(set1))


n = int(input("Enter a Number: "))

print("Even" if n % 2 == 0 else "Odd")

