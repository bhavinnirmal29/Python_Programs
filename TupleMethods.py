# Tuple Methods
# empty tuple
# Output: ()
my_tuple = ()
print(my_tuple)

# tuple having integers
# Output: (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
# Output: ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
print("Element 1 = ",my_tuple[1])

# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
# Output:
# 3
# 4.6
# dog
a, b, c = my_tuple
print(a)
print(b)
print(c)
############################################
my_tuple = ('p','e','r','m','i','t')

# Output: 't'
print(my_tuple[-1])

# Output: 'p'
print(my_tuple[-6])

##############################################
my_tuple = ('a','p','p','l','e',)

# Count
# Output: 2
print(my_tuple.count('p'))

# Index
# Output: 3
print(my_tuple.index('p'))
##############################
print("len()#############")
testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))

print("max()#########################")
# using max(arg1, arg2, *args)
print('Maximum is:', max(1, 3, 2, 5, 4))

# using max(iterable)
num = [1, 3, 2, 8, 5, 10, 6]
print('Maximum is:', max(num))

print("min()###################")
# using min(arg1, arg2, *args)
print('Minimum is:', min(1, 1,3, 2, 5, 4))

# using min(iterable)
num = [3, 2, 8, 5, 10,2, 6]
print('Minimum is:', min(num))
########################################
numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum = sum(numbers)
print(numbersSum)

# start = 10
numbersSum = sum(numbers, 10)
 
print(numbersSum)
##############################



