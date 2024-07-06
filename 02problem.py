"""
      Write a program to accept marks of 6 students and display them in a sorted 
       manner.
"""

marks=[]
m1=int(input("Enter marks m1: "))
marks.append(m1)
m2=int(input("Enter marks m2: "))
marks.append(m2)
m3=int(input("Enter marks m3: "))
marks.append(m3)
m4=int(input("Enter marks m4: "))
marks.append(m4)
m5=int(input("Enter marks m5: "))
marks.append(m5)
m6=int(input("Enter marks m6: "))
marks.append(m6)
print(marks)
print("\n\n")


print("Printing Sorted list")
marks.sort()
print(marks)