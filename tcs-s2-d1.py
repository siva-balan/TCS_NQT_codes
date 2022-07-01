arr = []
n = int(input())


count = 1
for i in range(n):
    ele = int(input())
    arr.append(ele)

max = arr[0]
for i in range(1,n):
    for j in range(0,i):
        if max < arr[j]:
            max = arr[j]
    if arr[i] > max:
        count +=1

print(count)
