'''Constructors in Python
Class functions that begins with double underscore (__)
are called special functions as they have special meaning.

Of one particular interest is the __init__() function.
This special function gets called whenever a new object of that class
is instantiated.

This type of function is also called constructors in
Object Oriented Programming (OOP).
We normally use it to initialize all the variables.
'''
class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5,6)
c2.attr = 10

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
#c1.attr
