num1=int(input('Enter 1st num:'))
num2=int(input('Enter 2nd num:'))
num3=int(input('Enter 3rd num:'))
max=num1 if num1>num2 and num1>num3 else num2 if num2>num3 else num3
print(max,'is maximum')
