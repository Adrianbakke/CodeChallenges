from copy import deepcopy
import heapq

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

input = open("input.txt", "r").read()

X = [list(x) for x in input.splitlines()]

R, C = len(X), len(X[0])

sr, sc, er, ec = 0, 0, 0, 0
for r in range(R):
    for c in range(C):
        if X[r][c] == "S":
            sr, sc = (r, c)
        elif X[r][c] == "E":
            er, ec = (r, c)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

H = [(0, 0, sr, sc, [(sr, sc)])]  # priority queue with (cost, dir, row, col, turns, moves, path)
best_cost = float('inf')
best_paths = []

# Track the best cost for each (row, col) to avoid redundant paths
best_cost_at = {}

while H:
    cost, d, r, c, path = heapq.heappop(H)

    if (r, c) == (er, ec):
        if cost < best_cost:
            best_cost = cost
            best_paths = [path]
        elif cost == best_cost:
            best_paths.append(path)
        continue

    # Check if this position has been visited with a lower or equal cost
    if (d, r, c) in best_cost_at and best_cost_at[(d, r, c)] < cost:
        #print(r,c)
        #exit()
        continue

    best_cost_at[(d, r, c)] = cost

    # Explore the next positions
    nr, nc = r + dirs[d][0], c + dirs[d][1]
    if 0 <= nr < R and 0 <= nc < C and X[nr][nc] != '#':
        heapq.heappush(H, (cost + 1, d, nr, nc, path + [(nr, nc)]))
    heapq.heappush(H, (cost + 1000, (d + 1) % 4, r, c, path))
    heapq.heappush(H, (cost + 1000, (d + 3) % 4, r, c, path))

unique_squares = set()
for path in best_paths:
    unique_squares.update(path)

# Create a deep copy of the original grid to mark unique squares
marked_grid = deepcopy(X)

# Mark the unique squares with a special character, e.g., '*'
for r, c in unique_squares:
    if marked_grid[r][c] not in ('S', 'E'):  # Avoid overwriting the start and end
        marked_grid[r][c] = '*'

# Print the marked grid
for row in marked_grid:
    print(''.join(row))
print(f"Best cost: {best_cost}")
print(f"Number of best paths: {len(best_paths)}")
print(f"Unique squares in best paths: {unique_squares}")
print(len(unique_squares))
