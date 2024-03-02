num=int(input('Enter a num:'))
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num//=10
    
    
print('the reverse of the number is:',rev)