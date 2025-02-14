foo =10;

def sample_function():
    foo=20;
    print(foo)
    def innner_function():
        nonlocal foo
        foo=50
        print(foo)
    innner_function()
    print(foo)
sample_function()
print(foo)