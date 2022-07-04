n =  int(input())

sign = 1
if n<0 :
    sign = -1
    x = str(n)
    z = x[1:]
    y = z[::-1]
    y = int(y.lstrip("0"))
    
else: 
    sign = 1
    x = str(n)
    y = x[::-1]
    y = int(y.lstrip("0"))

m = sign* y

if m> 32768 or m< -32768:
    print("Wrong value")
else:
    print(m)