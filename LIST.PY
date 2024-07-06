li=[2,8,6,3,4,75]
print(li)
# print(sum(li))

# #  List Slicing
# print(li[1:3])  # ----> print element from index 1 to 2

# print(li[0:6:2])  # ---> print element from  index 0 to 5 by step of element(lefting 1 element)

# print(li[-6:-1:2])

# print(li.sort())   #  ----->  this will return 'None'
# li.sort()  # this will sort the list
# print(li) 


li.reverse()  #---->  will reverse the link 
print(li)

li.append(98)  #  ----> this will add 98 to last of list
print(li)


li.insert(1,90)  # ----> this will add 90 at the the index 1
print(li)


print(li.pop(2)) # --->  this will remove an element which is at index 2 if index is out of range it will provide error


x=li.remove(90)  # ---> it will return None because it directly modifies the list
print(li)