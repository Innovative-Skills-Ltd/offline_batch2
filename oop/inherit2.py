class A:
    def __init__(self):
        print("A init")
    def sample(self):
        print("sample")

class B(A):
    def __init__(self):
        print("B init")
        A().sample()
        

class C(A):
    def __init__(self):
        print("C init") 
        A().__init__()

class D(B, C):
    def __init__(self):
        print("D init")
        B().__init__()
        C().__init__()  

d = D()

print(D.__mro__)