# Find the 15th term of the series?
# 0,0,7,6,14,12,21,18, 28
# Explanation :
# In this series the odd term is increment of 7 {0, 7, 14, 21, 28, 35 – – – – – – }
# And even term is a increment of 6 {0, 6, 12, 18, 24, 30 – – – – – – }
def find_num(n):
    if n%2==0:
        return int(((n/2)-1)*6)
    else:
        return (n//2)*7
    
print(find_num(15))