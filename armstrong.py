#It is an n-digit number is an Armstrong number if the sum of its individual digits,
#each raised to the power of n, is equal to the original number.
#For example, let's consider a 3-digit number 153:
#1^3+5^3+3^3=1+125+27=153

def armstrong(num):
    l=len(str(num))
    temp=num
    armstrong=0
    while num>0:
        d=num%10
        armstrong=armstrong+d**l
        num//=10
    
    if temp==armstrong:
        print(temp,' is armstrong number')
    else:
        print(temp,' is not armstrong number')

num=int(input('Enter number to find armstrong or not:'))
armstrong(num)
        
        