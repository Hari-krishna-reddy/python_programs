
#Certainly, let's consider an example to illustrate why checking divisibility up to
#the square root is sufficient.

#Suppose we want to check whether the number 36 is prime. The square root of 36 is 6.
#So, if 36 has a divisor greater than 6, it must also
#have a corresponding divisor smaller than or equal to 6.

#If 36 has a divisor greater than 6, say 9, then the corresponding divisor would be
#36 / 9 = 4. Since 4 is less than or equal to the square root of 36, we would have
#already checked it when iterating up to the square root.

import math
def isPrime(num):
    if num <=2:
        return 0
    else:
        for i in range(2,int(math.sqrt(num)+1)):
            if num%i==0:
                return 1
        return 0
num=int(input('enter a number to find it is prime or not:'))
ans=isPrime(num)
if ans:
    print(num,' is not prime')
else:
    print(num,' is prime')
    

                       