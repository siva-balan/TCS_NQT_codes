s = input()

count1, count2 = 0,0
for i in s:
    if i == '*':
        count1 += 1
    elif i == '#':
        count2 +=1
    else :
        print("invalid input")


print((count1 - count2))