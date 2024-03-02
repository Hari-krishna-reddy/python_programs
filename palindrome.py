def palindrome(num):
    temp=num
    reverse_num=0
    while num>0:
        d=num%10
        reverse_num=reverse_num*10+d
        num//=10
    if temp==reverse_num:
        return 1
    else:
        return 0
num=int(input('Enter number to find palindrome or not:'))
if palindrome(num):
    print(num,' is palindrome')
else:
    print(num,' is not apalindrome')
    