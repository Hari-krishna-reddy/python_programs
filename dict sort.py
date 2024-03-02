from collections import Counter
d=Counter([2,3,1,3,2])

d=dict(sorted(d.items(), key= lambda item:item[1]))
l=[]
for i in d:
    for k in range(d[i]):
        l.append(i)
print(l)
    