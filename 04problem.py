# 4 Write a program to sum a list with 4 numbers.
total=0
l1=[]
e1=int(input("Enter e1: "))
l1.append(e1)
e2=int(input("Enter e2: "))
l1.append(e2)
e3=int(input("Enter e3: "))
l1.append(e3)
e4=int(input("Enter e4: "))
l1.append(e4)

print(l1)

# total= sum(l1)
# print(total)


for i in range(0,len(l1)):
    total=total + l1[i]

print(total)
