n = int(input())
#01011


val= bin(n)
a = ""
for  i, x in enumerate(val[2:]):
    if x=='1': 
        a += '0'
    else:
        a += '1'

print(a)
print(int(a,2))

