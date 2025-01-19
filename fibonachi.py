a , b = 0, 1
while a<100:
    print(a, end=',')
    a , b = b, a+b





def fibonachi(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
        return result
fib=fibonachi(100)

     
