v =  int(input())
w = int(input())

if (w%2 != 0) or w<2 or v>w:
    print("INVALID INPUT")
else:
    x = ((4*v) -w)/2

print("TW ="+str(int(x))+" "+"FW ="+str(int(v-x)))