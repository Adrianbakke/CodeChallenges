from collections import deque
import sys
sys.setrecursionlimit(9999999)


input = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
X = input.splitlines()

X = open("input.txt", "r").read().splitlines()

R,C = len(X), len(X[0])

def get_neigh(row,col):
    dirs = ((1,0), (0,1), (-1,0), (0,-1))
    # slope = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}
    # if X[row][col] in slope.keys():
    #     r,c = slope[X[row][col]]
    #     return [(row+r,col+c)]

    res = []
    for r,c in dirs:
        if (0 <= col+c <= C-1) and (0 <= row+r <= R-1):
            if X[row+r][col+c] != "#":
                res.append((row+r, col+c))
    return res

sr,sc = 0,0
er,ec = R-1,0
for c in range(C):
    if X[0][c] == ".":
        sc = c
        break
for c in range(C):
    if X[-1][c] == ".":
        ec = c
        break


for x in X:
    print(x)
print(sr,sc,er,ec)


visited = [[False for _ in range(C)] for _ in range(R)]

import copy
# BFS from given source s
res = []

# to make faster save coords where paths split,
# keep only the longest chain who have reached that point so far
def dfs(coords):
    curr = coords[-1]
    neigh = get_neigh(*curr)
    #print("n neigh", len(neigh))
    for x in neigh:
        if len(coords)>1 and x in coords:
            continue
        if x == (er,ec):
            res.append(len(coords))
            print(x,len(coords))
            continue
        #if not visited[x[0]][x[1]]:
#          [x[0]][x[1]] = True
        n = copy.deepcopy(coords)
        n.append(x)
        dfs(n)

def bfs(r, c):
    # Create a queue for BFS
    q = deque()

    visited[r][c] = True
    q.append(((r,c)))

    # Iterate over the queue
    while q:
        # Dequeue a vertex from queue and print it
        print(len(q), end="\r")
        curr = q.popleft()
        coord = curr[-1]
        for x in get_neigh(coord[0], coord[1]):
            if len(curr)>1 and x == curr[-2]:
                continue
            if x == (er,ec):
                # n = copy.deepcopy(curr)
                # n.append(x)
                res.append(len(curr))
                continue
            #if not visited[x[0]][x[1]]:
#          [x[0]][x[1]] = True
            n = copy.deepcopy(curr)
            n.append(x)
            q.append(n)
    return q

gr = 0
def dfs2(coords, visited):
    global gr
    curr = coords[-1]
    neigh = get_neigh(*curr)
    for x in neigh:
        if x == (er, ec):
            if len(coords) > gr:
                res.append(len(coords))
                gr = len(coords)
                print(len(coords))
            continue
        if visited[x[0]][x[1]]:
            continue
        visited[x[0]][x[1]] = True
        coords.append(x)
        dfs2(coords, visited)
        coords.pop()  # Backtrack: Remove the last coordinate
        visited[x[0]][x[1]] = False  # Backtrack: Mark the cell as unvisited

visited = [[False for _ in range(C)] for _ in range(R)]
visited[sr][sc] = True
dfs2([(sr, sc)], visited)

print("start", sr, sc)
#q = bfs(sr,sc)
#dfs([(sr,sc)])

print(res)
print(len(res))

print(sorted(res))


