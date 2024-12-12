# thanks https://github.com/jonathanpaulson/AdventOfCode/blob/master/2024/12.py for part 2
from collections import defaultdict, deque

X = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

X = open("input.txt", "r").read()

B = [list(x) for x in X.splitlines()]

regs = set(xx for x in X.splitlines() for xx in x)

R,C=len(B),len(B[0])

def move(r,c):
    res = []
    for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        nr,nc = r+dr,c+dc
        if 0<=nr<R and 0<=nc<C:
            res.append((nr,nc))
    return res

seen = set()
grids = defaultdict(list)
areas = []
sides = []
for r in range(R):
    for c in range(C):
        if (r,c) in seen:
            continue
        Q = deque()
        #b = [(r,c)]
        b = []
        Q.append((r,c))
        edges = defaultdict(set)
        while Q:
            nr,nc = Q.popleft()
            if (nr,nc) in seen:
                continue
            seen.add((nr,nc))
            b.append((nr,nc))
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                if 0<=nr+dr<R and 0<=nc+dc<C and B[nr+dr][nc+dc]==B[r][c]:
                    Q.append((nr+dr,nc+dc))
                else:
                    edges[(dr,dc)].add((nr,nc))
        areas.append(len(b))

        side = 0
        for k,v in edges.items():
            seen_edges = set()
            for rr,cc in v:
                if (rr,cc) in seen_edges:
                    continue
                #seen_edges.add((rr,cc))
                side +=1
                Q = deque([(rr,cc)])
                while Q:
                    nr,nc = Q.popleft()
                    if (nr,nc) in seen_edges:
                        continue
                    seen_edges.add((nr,nc))
                    for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                        dr,dc=nr+dr,nc+dc
                        if (dr,dc) in v:
                            Q.append((dr,dc))
        sides.append(side)

print(areas)
print(sides)

res = 0
for x,y in zip(areas,sides):
    res += x*y
print(res)