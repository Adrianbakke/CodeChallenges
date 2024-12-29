import sys
from collections import defaultdict

# Set the maximum recursion depth to a higher value, for example, 3000
sys.setrecursionlimit(30000)

# Your recursive function or code goes here
input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

X = [list(x) for x in input.splitlines()]

R,C=len(X),len(X[0])

start,end=None,None
for r in range(R):
    for c in range(C):
        if X[r][c] == "S":
            start = (r,c)
        elif X[r][c] == "E":
            end = (r,c)

moves = {"l":(0,-1), "d":(1,0), "r":(0,1), "u":(-1,0)}

from copy import deepcopy

def dfs_maze(X, start, end):
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(r, c):
        return X[r][c] != '#'

    visited = set()
    v = defaultdict(int)
    results = []
    def dfs(r, c, dir_idx, score, moves):
        # print("\n".join("".join(x) for x in X))
        dir_idx = dir_idx%4
        if (r, c) == end:
            results.append([score, moves])
            return
        if v[(r,c)] < score:
            return

        v[(r,c)] += score
        #if (dir_idx, r, c) in visited: return

        #min_score = float('inf')

        # Try moving forward in the current direction
        nr, nc = r + directions[dir_idx][0], c + directions[dir_idx][1]

        #X[r][c] = '#'  # Mark as visited
        #visited.add((dir_idx, r, c))

        if (0<=r<R and 0<=c<C) and is_valid(nr,nc):
            dfs(nr, nc, dir_idx, score+1, deepcopy(moves)+[(dir_idx, r, c)])
        dfs(r, c, dir_idx+1, score+1000, deepcopy(moves)+[(dir_idx, r, c)])
        dfs(r, c, dir_idx-1, score+1000, deepcopy(moves)+[(dir_idx, r, c)])

        return

    # Starting from 'S', initially facing right (index 0)
    initial_direction = 0
    dfs(start[0], start[1], initial_direction, 0, [])
    return results

# Call the function with the given maze input
results = dfs_maze(X, start, end)


# def stack():
#     Q = [(0,start)]
#     seen = set()
#     while Q:
#         curr = Q.pop()

s,visited = sorted(results)[0]
print(s)
for d,r,c in visited:
    print(d,r,c)
    X[r][c] = ['r','d','l','u'][d]


print("\n".join("".join(x) for x in X))

