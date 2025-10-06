

class A:
    def __init__(self):
        print("this is parent constructor")
    def sample_method(self):
        print("this is parent sample method")

class A1(A):
    def __init__(self,x):
        print(x)
        print("this is child constructor")
    def sample_method(self):
        A().sample_method()
        print("this is child sample method")
a1 = A1(10)
a1.sample_method()