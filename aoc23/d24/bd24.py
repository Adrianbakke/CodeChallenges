import numpy as np

with open("input.txt", "r") as f:
    input = f.read().splitlines()

input = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

input = input.splitlines()

N = len(input)

nano = 1e-9
step = lambda x: nano*x
print(nano)


print(N)

x1,x2 = input[:2]

p,v = x1.split("@")
px,py,pz = list(map(int, p.split(",")))
vx,vy,vz = list(map(int, v.split(",")))

p1 = np.array([px, py, pz])
v1 = np.array([vx, vy, vz])

p,v = x2.split("@")
px2,py2,pz2 = list(map(int, p.split(",")))
vx2,vy2,vz2 = list(map(int, v.split(",")))

p2 = np.array([px2, py2, pz2])
v2 = np.array([vx2, vy2, vz2])

def get_lines():
    lines = []
    for i in input:
        p,v = i.split("@")
        lines.append([np.array(list(map(int, p.split(",")))), np.array(list(map(int, v.split(","))))])
    return lines

pairs = []
for n,i in enumerate(input[:-1]):
    for ii in input[n+1:]:
        pairs.append([i,ii])

def valid_line(p,v):
    for x in input:
        pp,vv = x.split("@")
        p1 = np.array(list(map(int, pp.split(","))))

        v1 = np.array(list(map(int, vv.split(","))))

        p1 = np.array([px, py])
        v1 = np.array([vx, vy])

        norm = (vx2*vy)-(vy2*vx)
        if norm == 0: 
            continue

        t = (vx*(py2-py))-(vy*(px2-px))
        t = t/norm
        if t <= 0:
            print("past B")
            continue
        s = (px2-px+vx2*t)/vx
        if s <= 0:
            print("past A")
            continue

        h = p2+v2*t

        if all(200000000000000<=x<=400000000000000 for x in h):
            res += 1


for s1 in range(1,N+2):
    for s2 in range(1,N+2):
        r1 = p1+v1*s1
        r2 = p2+v2*s2
        v = (r2-r1)/(s1-s2)
        if s1 > s2:
            v = -1*v
        p = r2-v*s2
        valid_line(p,v)

def valid_line(p,v):
    lines = get_lines()
    for lr, lv in lines:
        for n in (1,N+2):
            r = lr + lv * n
