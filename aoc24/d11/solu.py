from collections import defaultdict
from copy import deepcopy

X = "0 1 10 99 999"

X = open("input.txt", "r").read()
X = X.split(" ")

d = defaultdict(int)

for i in range(len(X)):
    d[X[i]] += 1

for _ in range(75):
    t = defaultdict(int)
    for k,v in d.items():
        if int(k)==0:
            #t[k] = 0
            t["1"] += v 
        elif len(k)%2==0 and len(k)>1:
            lh = str(int(k[:len(k)//2]))
            rh = str(int(k[len(k)//2:len(k)]))
            #t[k] = 0
            t[lh] += v
            t[rh] += v
        else:
            #t[k] = 0
            t[str(int(k)*2024)] += v
    d = deepcopy(t)

print(len(d))
print(sum([v for k,v in d.items()]))
