tup=(1,2)
match tup:
    case(0,0):
        print('Origin')
    case(1,x):
        print(x)
    case(x,y):
        print(x+y)
    case _:
        print('blah')