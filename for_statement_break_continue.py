
for n in range(2,10):
    for m in (range(2,n)):
        if n%m ==0:
            print(n,'equals',m,'*',n//m)
            break
        else:
            print(n,'it is prime number')