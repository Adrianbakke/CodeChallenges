X = open("input.txt", "r").read().splitlines()

l1,l2 = [],[]
for x in X:
    x1,x2 = x.split("   ")
    l1.append(int(x1))
    l2.append(int(x2))
from collections import defaultdict
s = defaultdict(int)

for x in l1:
    if s[x] == 0:
        s[x] = sum([xx for xx in l2 if xx == x])
    else:
        s[x] += s[x]

print(sum(abs(x1-x2) for x1,x2 in zip(sorted(l1), sorted(l2))))

print(s)

print(sum([v for v in s.values()]))

