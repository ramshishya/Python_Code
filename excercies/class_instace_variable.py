class Dog:
    kind=   'canine'
    tricks=[]
    def __init__(self,name):
        self.name=name
    def add_tricks(self,trick):
        self.tricks.append(trick)

d=Dog('Dog Name')

print(Dog.kind)
print(d.kind)
print(d.name)

