X = [list(map(int, x.split(" "))) for x in open("input.txt", "r").read().splitlines()]

def diff(x):
    return [x1-x2 for x1,x2 in zip(x[:-1], x[1:])]

def test(seq):
    if all([e != 0 for e in seq]) and all([0<abs(e)<4 for e in seq]):
        return all(seq[c-1]/abs(seq[c-1]) == seq[c]/abs(seq[c]) for c in range(1,len(seq)))
    return False

res = 0
for x in X:
    if test(diff(x)):
        res += 1
        continue
    for j in range(len(x)):
        seq = diff(x[:j]+x[j+1:])
        if test(seq):
            res += 1
            break

print(res)

