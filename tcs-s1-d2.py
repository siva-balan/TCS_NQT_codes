t = int(input())

e = []
l = []
balance = 0
remaining = 0

# a = list(map(int, input().split()) 
# can be used for single line input
for i in range(t):
    e.append(int(input()))

print("enter value of array L")
for i in range(t):
    l.append(int(input()))

for i in range(t):
    balance += e[i] - l[i]
    if remaining < balance:
        remaining = balance

print(remaining)