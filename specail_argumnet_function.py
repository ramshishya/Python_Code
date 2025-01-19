def test_function(argument1,*argument2,**argument3):
    print(argument1)
    print(argument2)
    print(argument3)
test_function(1,2,3,name= 'Ram',foo ='FOOOD')


#function with specail parameter 
def positional_argument(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)
positional_argument(*range(1,4))