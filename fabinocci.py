n=int(input('Enter number od fibonacci numbers:'))
n1=0
n2=1
count=2
print(n1)
print(n2)
while count<=n:
    n3=n1+n2
    n2=n3
    n1=n2
    print(n3)
    count+=1