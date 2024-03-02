# Problem 4: Bastin once had trouble finding the numbers in a string.
# The numbers are distributed in a string across various test cases.
# There are various numbers in each test case you need to find the number in each test case.
# Each test case has various numbers in sequence. You need to find only those numbers which do not contain 9.
# For eg, if the string contains "hello this is alpha 5051 and 9475".
# You will extract 5051 and not 9475.
# You need only those numbers which are consecutive and you need to help him find the numbers.
# Print the largest number.
# Note: Use long long for storing the numbers from the string.
# Input:
# 
# The first line consists of T test cases and the next T lines contain a string.
# 
# Output:
# 
# For each string output the number stored in that string
# if various numbers are there print the largest one. If a string has no numbers print -1.

def largest_num(s):
    l=len(s)-1
    i=0
    ans=[]
    while i<=l:
        j=i
        num=''
        if s[i].isdigit():
            num+=s[i]
            while j<l and s[j+1].isdigit():
                j=j+1
                i+=1
                
                num+=s[i]
            ans.append(num)
    
        i+=1
    for i in ans:
        if '9' in i:
            ans.remove(i)
    print(max([int(x) for x in ans]))
    
            
largest_num("a 5051 and 9475 as 1234 is busy 121")