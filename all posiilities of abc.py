from itertools import permutations
string='abc'
perm=permutations(string,)
for i in perm:
   print(''.join(i))