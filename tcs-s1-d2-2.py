''' At a fun fair, a street vendor is selling different colours of balloons. He sells N number of different colours of balloons (B[]). 
The task is to find the colour (odd) of the balloon which is present odd number of times in the bunch of balloons.

Note: If there is more than one colour which is odd in number, then the first colour in the array which is present odd number of times is displayed. 
The colours of the balloons can all be either upper case or lower case in the array. 
If all the inputs are even in number, display the message “All are even”.'''


import sys
n = int(input())
b = []

dummy = 0
for i in range(n):
    b.append(input())

b = [x.lower() for x in b]
for i in range(n):
    count = 0
    for j in range(n):
        if b[i] == b[j]:
            count +=1
    if count % 2 != 0:
        print(b[i])
        dummy +=1
        sys.exit()

if dummy == 0:
    print("All are even")
