class A:
    def __init__(self):
        self.var1 = 100

    def display1(self, var1):
        print("CLASS A: ", self.var1)


class B(A):
    def display2(self, var1):
        print("CLASS B: ", self.var1)


obj = B()
obj.display1(200)
