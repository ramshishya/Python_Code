squares =[]
for x in range(20):
    squares.append(x**2)
    print(squares[x])

##List Compreshension 

print('List Compreshension')
square=[x**2 for x in range(20)]
print(square[x])



vec=[[1,2],[20,21],[10,13],[1,4]]

[num for elm in vec for num in elm]
print(num)