fruits = ['Apple','Orange','Mango','Apple','Orange','graps']
numbers=[1,2,3,4,5,6,7,8,8,2,3,4,5,6]

print(fruits)
fruits.sort()
print(fruits)

print(fruits.count('Apple'))


#List as queueu 

from collections import deque
queue=deque(['Eric','John','Michal'])
queue.append('ramshishya')
queue.append('timtim')

print(queue)

queue.popleft()
print(queue)

