t1=()   # Tuples are immutable
print(type(t1))
t2=(2,4,"apple", False,True,"banana")
print(t2)


# Tuple methods

# 1 tuple.count(4)----> return no time occurance 4 in tuple
no= t2.count(4)
print(no)

# 2 tuple.index(2) # Returns the index of the first occurrence of a specified value 
# in the tuple. Raises a ValueError if the value is not found.
print(t2.index("banana"))

i=t2.index(False)
print(i)








mytuple=(1,2,3)
a,b,c = mytuple
print(a,b,c)