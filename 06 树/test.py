class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def print_a(self):
        print(self)

c = test(0,1)
c.print_a()