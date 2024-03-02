# Problem 1: Write a program to find the count of numbers that consists of unique digits.
# Input:
# 
# Input consists of two Integer lower and upper values of a range
# 
# Output:
# 
# The output consists of a single line and prints the count of unique digits in a given range. Else Print"No Unique Number"
# 
# Solution:
# 
# Input -
# 
# 10
# 
# 15

# 10 11 12 13 14 15 here 0,2,3,4,5 are unique so output is 5
def count(i,l):
    while i>0:
        d=i%10
        i//=10
        if d in l:
            l.remove(d)
            break
        else:
            l.append(d)
    return l


def unique(n,m):
    l=[]
    for i in range(n,m+1):
        l=count(i,l)
    print(len(l))
    
unique(10,16)
          
        
        
        





















