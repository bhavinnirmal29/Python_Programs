class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self,x):
        return Vector(self.a + x.a, self.b + x.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
v3 = Vector(3,2)
print (v1 + v2 + v3)

'''
1-File
2-Exception
---------------
1- oops - done
2- gui programming
3- Database
4- requlerExpresion


'''
