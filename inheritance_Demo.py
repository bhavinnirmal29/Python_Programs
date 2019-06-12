class A:
    def a():
        print("Class A")
class B(A):
    def b():
        print("Class B")
    def a():
        print("Class B")

ob1 = A
ob1.a()
ob =B
ob.a()
ob.b()
