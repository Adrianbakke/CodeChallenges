from copy import deepcopy


X = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

X = open("input.txt", "r").read().splitlines()

X = [list(x) for x in X]

R,C = len(X), len(X[0])
def startpos():
    for r in range(R):
        for c in range(C):
            if X[r][c] == "^":
                X[r][c] = "u"
                return (r,c)

sr,sc = startpos()

def turn(x):
    d = {"u": "r", "r": "d", "d": "l", "l": "u"}
    return d[x]


# def move(r,c, seen):
#     dir = X[r][c]
#     d = {"u": (-1,0), "r": (0,1), "d": (1,0), "l": (0,-1)}
#     dr, dc = d[dir]
#     if not (0<=r+dr<R and 0<=c+dc<C):
#         return r+dr, c+dc, False, seen
#     if X[r+dr][c+dc] == "#":
#         seen[(r, c, dr, dc)] += 1
#         if seen[(r, c, dr, dc)] > 8:
#             return r, c, True, seen
#         X[r][c]=turn(X[r][c])
#         dr,dc = d[X[r][c]]
#         dir = X[r][c]
#     X[r+dr][c+dc]=dir
#     X[r][c]="X"
#     return r+dr,c+dc,False, seen


from collections import defaultdict
res = set()
p2 = 0
print(sr,sc)
for r in range(R):
    for c in range(C):
        if (r,c) == (sr,sc):
            continue
        print(r," /130", end="\r")
        seen = set()
        #X = deepcopy(XX)
        #X[r][c] = "#"
        #nr,nc,inf,seen = move(sr,sc,seen)
        d = 0
        nc,nr = sc,sr
        while True:
            #nr,nc,inf,seen = move(nr,nc, seen)
            dir = [(-1,0), (0,1), (1,0), (0,-1)]
            dr, dc = dir[d]
            if not (0<=nr+dr<R and 0<=nc+dc<C):
                break
            if X[nr+dr][nc+dc] == "#" or nr+dr==r and nc+dc==c:
                d = (d+1)%4
                continue
            nr,nc = nr+dr,nc+dc
            if (nr,nc,d) in seen:
                p2 += 1
                break
            seen.add((nr,nc,d))

print("hello")
print(p2)
