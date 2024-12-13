import numpy as np

X = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
X = open("input.txt", "r").read()
X = [x.split("\n") for x in X.split("\n\n")]
inst = []
for x in X:
    d = dict()
    for xx in x:
        a,b = xx.split(": ")
        if a == "Prize":
            c=10000000000000 
        else:
            c=0
        d[a]=list(map(lambda x: int(x[2:])+c, b.split(", ")))
    inst.append(d)

def solve(ax, ay, bx, by, px, py):
    m = np.array([[bx,ax-bx],[by, ay-by]], dtype=np.float64)
    x = np.array([px,py], dtype=np.float64 )
    #n,k = list(map(int, (np.linalg.solve(m,x))))
    n,k = np.linalg.solve(m,x)
    N = round(n)
    K = round(k)

    if N < 0 or K < 0:
        return 0,0
    if px==K*ax+(N-K)*bx and py==K*ay+(N-K)*by:
        return 3*K, N-K
    else:
        return 0,0


res = []
for e in inst:
    ax,ay=e["Button A"]
    bx,by=e["Button B"]
    px,py=e["Prize"]
    def _inner():
        N = 200
        for i in range(N):
            #print(i)
            if px-(i*ax)-((N-i)*bx) == 0 and py-(i*ay)-((N-i)*by) == 0:
                return i*3,N-i
        return (0,0)
    #res.append(sum(_inner()))
    res.append(sum(solve(ax, ay, bx, by, px, py)))

print(res)
print(sum(res))