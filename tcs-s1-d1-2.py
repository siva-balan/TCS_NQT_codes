""" Given a string S(input consisting) of ‘*’ and ‘#’. The length of the string is variable. 
The task is to find the minimum number of ‘*’ or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ and ‘#’ are equal. 
The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ and ‘#’ in the input string."""

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
