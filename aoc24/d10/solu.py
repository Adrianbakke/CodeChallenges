from collections import deque, defaultdict
from copy import deepcopy


X = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

X = open("input.txt", "r").read()

X = [list(map(int, list(x))) for x in X.splitlines()]
print(X)

R,C = len(X), len(X[0])

zeropos = [[r,c] for r in range(R) for c in range(C) if X[r][c] == 0]

def move(r,c):
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    res = []
    for dr,dc in dirs:
        nr,nc = r+dr,c+dc
        if 0<=nr<R and 0<=nc<C:
            res.append((nr,nc))
    return res

res = defaultdict(list)
res2 = defaultdict(int)
for count, (r,c) in enumerate(zeropos):
    Q = deque()
    Q.append([(r,c)])
    while Q:
        co = Q.popleft()
        nr = co[-1][0]
        nc = co[-1][1]
        if X[nr][nc] == 9:
            res[count].append(deepcopy(co))
            res2[(nr,nc,count)] += 1
        else:
            for rr,cc in move(nr,nc):
                if (rr,cc) not in co and X[rr][cc]==X[nr][nc]+1:
                    c = deepcopy(co)
                    c = c + [(rr,cc)]
                    Q.append(c)

r = 0
for k,v in res.items():
    c = []
    for i in range(len(v)):
        if v[i][-1] not in c:
            c.append(v[i][-1])
    r += len(c)

print(r)

r = 0
for k,c in res2.items():
    print(c)
    r+=c

print(r)


