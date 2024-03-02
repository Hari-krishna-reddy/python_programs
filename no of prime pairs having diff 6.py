# There is a range given n and m in which we have to find the count of all the prime pairs whose difference is 6. We have to find how many sets are there within a given range.
# Output:
# 
# The output consists of a single line and prints the count of prime pairs in a given range. Else print"No Prime Pairs".
# 
# Constraints:
# 
# 2<=n<=1000
# 
# n<=m<=2000
# 
# Sample Input:
# 
# 4
# 
# 30
# 
# Output:
# 
# 6
# 
# Explanation:4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
# 
# (5, 11) (7, 13) (11, 17) (13, 19) (17, 23) (23, 29). we have 6 prime pairs.
import math
def prime(num):
    if num <=2:
        return 0
    else:
        for i in range(2,int(math.sqrt(num)+1)):
            if num%i==0:
                return 1
        return 0

    


def prime_pairs(n,m):
    l=[]
    ans=[]
    for i in range(m-6-n+1):
         l.append((i+n,i+n+6))
    print(l)
    for j in l:
        if prime(j[0]):
            continue
        elif not prime(j[1]):
            ans.append((j[0],j[1]))
            
    print(ans,len(ans))
         
        
    
    
prime_pairs(4,30)
        
        





















