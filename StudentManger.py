"""

1: Student Enrolment Manager: Create a python code to domonstrate the use of sets and perform set operations (union, insterction, differnce) to manage student enrollments in multiple courses / appearing for multiple entarance exams like CET, JEE, NEET etc.



CET = {"Steve", "Jensen", "Vishal", "Suraj", "Elon"}

JEE = {"Elon", "Larry", "Bill", "Steve", "Mark", "Jeff", "Jensen", "Warren", "Sergey"}

NEET = {"Mark", "Ranjit", "Elon", "Suraj", "Sergey", "Vishal", "Bill", "Yash"}

# print(Students1.union(Students2))   # Every name will print atleat once

# k = Students1.union(Students2)
# print(k)

# print(Students1.intersection(Students2))    # The name which is common in both 

# print(Students1.difference(Students2))  # The name which is same in both will not print

# print(Students2.difference(Students1))

all_students = CET.union(JEE, NEET)
print("\nStudnets apperaring for atleast one exam: ")
print(all_students)

cet_jee = CET.intersection(JEE)
print("\nStudent appearing for both CET and JEE exam: ")
print(cet_jee)

cet_neet = CET.intersection(NEET)
print("\nStudent appearing for both CET and NEET exam: ")
print(cet_neet)

jee_neet = JEE.intersection(NEET)
print("\nStudent appearing for both JEE and NEET exam: ")
print(jee_neet)

# only_cet = CET.difference(JEE, NEET)
# print("\nStudents only apperaring for CET")
# print(only_cet)

"""


'''

2: Student Record Keeper: Write a python program to crete, update and manipulate a dictionary of students records, including their grades and attendance.

'''

Students = {
    "name" : "Suraj Nisad",
    "Roll no." : 636,
    "Course" : "BTech",
    "College" : "AP Shah" 
}

Students.update({"Suraj" : "Chutiya"})
Students.pop("Course")

for key, value in Students.items():
    print(key, ":" , value)


x = Students.get("Roll no.")
print(x)

y = Students.keys()
print(y)

z = Students.values()
print(z)