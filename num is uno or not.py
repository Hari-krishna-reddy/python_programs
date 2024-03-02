# 1. Sum of the digits of the given positive integer number N is UNO or not.
# Problem Statement
# 
# Given a positive integer number N, reduce the number of digits of N by computing
# the sum of all the digits to get a new number. If this new number exceeds 9, then sum the digits of
# this new number to get another number and continue this way until a single digit value is obtained
# as the ‘digit sum’. The task here is to find out whether
# the result of the digit sum done this way is ‘1’ or not. If the result is 1 return UNO else not.






def sum_no(num):
    s=0
    while num>0:
        d=num%10
        s+=d
        num//=10
    return s
        
def uno(num):
    while num>10:
        num=sum_no(num)
    if num==1:
        print('uno')
    else:
        print('not uno')
uno(121213634654394723983723893434876384623)
    
        