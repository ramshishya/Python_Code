class myClass:
    """This is my first python class"""
    foo=10
    def print_foo():
        print("From Method")
    def __init__(self,initValue):
        self.foo=initValue

print(myClass.__doc__)
print(myClass.foo)
x=myClass(100)
print(x.foo)
x.foo=50
print(myClass.foo)