input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

input = open("input.txt","r").read()

X = input.splitlines()

def check4sym(m,n, lnum, num):
    print(m,n, lnum, num)
    if m-1>=0:
        for i in range(lnum+2):
            if 0<=n-1+i<N:
                if X[m-1][n-1+i] != "." and not X[m-1][n-1+i].isnumeric():
                    return True
    if m+1<M:
        for i in range(lnum+2):
            if 0<= n-1+i < N:
                if X[m+1][n-1+i] != "." and not X[m+1][n-1+i].isnumeric():
                    return True
    if n-1>=0:
        if X[m][n-1] != "." and not X[m][n-1].isnumeric():
            return True
    if n+lnum<N:
        if X[m][n+lnum] != "." and not X[m][n+lnum].isnumeric():
            return True
    return False

def check4gear(m,n, lnum, num):
    print(m,n, lnum, num)
    if m-1>=0:
        for i in range(lnum+2):
            if 0<=n-1+i<N:
                if X[m-1][n-1+i] == "*":
                    return True, (m-1,n-1+i)
    if m+1<M:
        for i in range(lnum+2):
            if 0<= n-1+i < N:
                if X[m+1][n-1+i] == "*":
                    return True, (m+1, n-1+i)
    if n-1>=0:
        if X[m][n-1] == "*":
            return True, (m, n-1)
    if n+lnum<N:
        if X[m][n+lnum] == "*":
            return True, (m, n+lnum)
    return False, ()

from collections import defaultdict
d = defaultdict(list)
res = []
M,N = len(X),len(X[0])
print(M,N)
m = 0
while m < M:
    n = 0
    while n < N:
        lnum = 0
        num = ""
        s = n
        while n<N and X[m][n].isnumeric():
            num += X[m][n]
            n += 1
        t,c = check4gear(m,s,len(num),num)
        if num!="" and t:
            if num.isnumeric():
                d[c].append(num)
        n += 1
    m+=1
print(d)

import math
res = []
for k,v in d.items():
    if len(v)>1:
        res.append(math.prod(map(int, v)))
print(sum(res))