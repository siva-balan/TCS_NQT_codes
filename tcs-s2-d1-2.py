r = int(input())
c = int(input())

matrix= []
sum = 0
max = 0
rno = 0
for i in range(0,r):
    a = []
    for j in range(c):
        x = int(input())
        a.append(x)
        sum+=x
    if sum > max:
        max = sum
        rno = i+1
    matrix.append(a)

print(rno)     

''' A parking lot in a mall has RxC number of parking spaces. Each parking space will either be  empty(0) or full(1). 
The status (0/1) of a parking space is represented as the element of the matrix. 
The task is to find index of the prpeinzta row(R) in the parking lot that has the most of the parking spaces full(1).'''
