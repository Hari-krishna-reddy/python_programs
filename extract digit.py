def extract(num):
    l=[]
    while num>0:
        l.insert(0,num%10)
        num//=10
    print(l)
    
extract(12003)
        