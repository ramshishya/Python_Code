try:
    raise ZeroDivisionError('foo',10) 
except ZeroDivisionError as err:
    print('Zero is not divided by number')
    print(err.args)