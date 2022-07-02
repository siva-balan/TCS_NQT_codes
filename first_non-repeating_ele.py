import sys
class Solution:
    def firstNonRepeating(self, arr, n): 
        for i in range(n):
            count = 0
            for j in range(n):
                if arr[i] == arr[j] :
                    count +=1
                    
            if count == 1:
                return arr[i]
                sys.exit()