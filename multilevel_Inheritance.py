class A:
    def a():
        print("Class A")
class B(A):
    def b():
        print("Class B")
class C(B):
    def c():
        print("Class C")

ob =C
ob.a()
ob.b()
ob.c()
