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

B = [list(x) for x in X.splitlines()]
R, C = len(B), len(B[0])

# Identify all unique region characters
regs = set(xx for x in B for xx in x)

def neighbors(r, c):
    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C:
            yield nr, nc

seen = set()
grids = defaultdict(list)

# Find connected components for each region character
for reg in regs:
    for r in range(R):
        for c in range(C):
            if (r, c) not in seen and B[r][c] == reg:
                Q = deque([(r,c)])
                seen.add((r,c))
                comp = [(r,c)]
                while Q:
                    nr, nc = Q.popleft()
                    for rr, cc in neighbors(nr, nc):
                        if (rr, cc) not in seen and B[rr][cc] == reg:
                            seen.add((rr, cc))
                            comp.append((rr, cc))
                            Q.append((rr, cc))
                grids[reg].append(comp)

def get_boundary_segments(cells):
    cell_set = set(cells)
    edges = set()
    # Each cell contributes up to four potential boundary edges:
    # For a cell at (r,c):
    # top edge: ((r,c), (r,c+1))
    # bottom edge: ((r+1,c), (r+1,c+1))
    # left edge: ((r,c), (r+1,c))
    # right edge: ((r,c+1), (r+1,c+1))
    
    for (r, c) in cells:
        # Top edge
        if (r-1, c) not in cell_set:
            edges.add(((r, c), (r, c+1)))
        # Bottom edge
        if (r+1, c) not in cell_set:
            edges.add(((r+1, c), (r+1, c+1)))
        # Left edge
        if (r, c-1) not in cell_set:
            edges.add(((r, c), (r+1, c)))
        # Right edge
        if (r, c+1) not in cell_set:
            edges.add(((r, c+1), (r+1, c+1)))

    # Separate horizontal and vertical edges and attempt to merge them
    horizontal_edges = defaultdict(list) # key: row, value: list of (c_start, c_end)
    vertical_edges = defaultdict(list)   # key: column, value: list of (r_start, r_end)

    for e in edges:
        (r1, c1), (r2, c2) = e
        if r1 == r2:
            # Horizontal edge
            row = r1
            c_start, c_end = sorted([c1, c2])
            horizontal_edges[row].append((c_start, c_end))
        else:
            # Vertical edge
            col = c1
            r_start, r_end = sorted([r1, r2])
            vertical_edges[col].append((r_start, r_end))

    def merge_intervals(intervals):
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge overlapping or adjacent intervals
                merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        return merged

    # Merge horizontal edges
    for r_key in horizontal_edges:
        horizontal_edges[r_key] = merge_intervals(horizontal_edges[r_key])

    # Merge vertical edges
    for c_key in vertical_edges:
        vertical_edges[c_key] = merge_intervals(vertical_edges[c_key])

    # Count total segments (each merged interval is one segment)
    total_segments = sum(len(v) for v in horizontal_edges.values()) + sum(len(v) for v in vertical_edges.values())

    return total_segments

# Calculate and print results
res = []
for g, reg_list in grids.items():
    for comp in reg_list:
        segments = get_boundary_segments(comp)
        res.append((g, segments))

print(res)
