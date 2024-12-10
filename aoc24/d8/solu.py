X = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()


X = open("input.txt", "r").read().splitlines()



R, C = len(X), len(X[0])

from collections import defaultdict
freq = defaultdict(list)

for r in range(R):
    print(X[r])
    for c in range(C):
        if X[r][c] not in ["#", "."]:
            freq[X[r][c]].append((r, c))

print()

for k, v in freq.items():
    for i in range(len(v)):
        for j in range(i+1,len(v)):
            x1 = v[i]
            x2 = v[j]
            dr, dc = x2[0] - x1[0], x2[1] - x1[1]

            # Calculate steps for filling in between
            r1,c1,r2,c2=x2[0],x2[1],x1[0],x1[1]
            while True:
                c = 0
                r1 += dr
                c1 += dc
                r2 += dr * -1
                c2 += dc * -1
                if 0 <= r1 < R and 0 <= c1 < C:
                    X[r1] = X[r1][:c1] + '#' + X[r1][c1 + 1:]
                else:
                    c +=1
                if 0 <= r2 < R and 0 <= c2 < C:
                    X[r2] = X[r2][:c2] + '#' + X[r2][c2 + 1:]
                else:
                    c +=1
                if c == 2: break

res = 0
for line in X:
    print(line)
    for x in line:
        if x!=".":
            res+=1
print(res)
