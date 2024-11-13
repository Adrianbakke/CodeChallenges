with open("input.txt", "r") as f:
    input = f.read().splitlines()

# input = """19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3"""

# input = input.splitlines()

pairs = []
for n,i in enumerate(input[:-1]):
    for ii in input[n+1:]:
        pairs.append([i,ii])

import numpy as np


res = 0
print(len(pairs))

for x1,x2 in pairs:
    # print()
    # print(x1)
    # print(x2)

    p,v = x1.split("@")
    px,py,pz = list(map(int, p.split(",")))
    vx,vy,vz = list(map(int, v.split(",")))

    p1 = np.array([px, py])
    v1 = np.array([vx, vy])

    p,v = x2.split("@")
    px2,py2,pz2 = list(map(int, p.split(",")))
    vx2,vy2,vz2 = list(map(int, v.split(",")))
    p2 = np.array([px2, py2])
    v2 = np.array([vx2, vy2])

    # check angle between v vectors to know if they will collide <0<pi

    #p1 = ax+c, p2 = bx + d

    norm = (vx2*vy)-(vy2*vx)
    if norm == 0: 
        continue

    t = (vx*(py2-py))-(vy*(px2-px))
    t = t/norm
    # print("t:", t)
    if t <= 0:
        print("past B")
        continue
    s = (px2-px+vx2*t)/vx
    # print("s:", s)
    if s <= 0:
        print("past A")
        continue

    h = p2+v2*t

    # print(t)

    # if all(7<=x<=27 for x in h):
    #     print("HIT!")
    if all(200000000000000<=x<=400000000000000 for x in h):
        res += 1


print(res)


