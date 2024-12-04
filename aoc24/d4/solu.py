X = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()
X = open("input.txt", "r").read().splitlines()

print(X)
R,C=len(X),len(X[0])
W = "XMAS"
W2 = "MAS"
res = 0
def find_xmas(r,c):
    global res
    l = len(W)
    #right
    if c+l-1 < C:
        col = X[r][c:c+l]
        if (col == W or col[::-1] == W):
            res+=1

    # bottom
    if r+l-1 < R:
        col = "".join([X[r+i][c] for i in range(l)])
        if (col == W or col[::-1] == W):
            res+=1

    # diag left
    if r+l-1 < R and c-l+1 >= 0:
        col = "".join([X[r+i][c-i] for i in range(l)])
        if (col == W or col[::-1] == W):
            res+=1

    # diag right
    if r+l-1 < R and c+l-1 < C:
        col = "".join([X[r+i][c+i] for i in range(l)])
        if (col == W or col[::-1] == W):
            res+=1

def find_x_mas(r,c):
    global res
    l = len(W2)
    s=c+2
    t = 0
    if s < R and r+l-1<C:
        col = "".join([X[r+i][c+i] for i in range(l)])
        if (col == W2 or col[::-1] == W2):
            print(col)
            t += 1

        col = "".join([X[r+i][s-i] for i in range(l)])
        if (col == W2 or col[::-1] == W2):
            t += 1
    if t==2: res+=1

for r in range(R):
    for c in range(C):
        find_x_mas(r,c)

print(res)
