import numpy as np

X = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""".splitlines()

for x in X:
    s2l = lambda x: np.array(list((map(int, x.split(',')))))
    f,s = map(s2l, x.split("~"))

def overlap(x1, x2):
    overlaps = []
    for xx1, xx2 in zip(x1, x2):
        s1, e1 = xx1.reshape(2, -1)
        s2, e2 = xx2.reshape(2, -1)

        # Calculate overlap in each dimension
        overlap_x = max(0, min(e1[0], e2[0]) - max(s1[0], s2[0]))
        overlap_y = max(0, min(e1[1], e2[1]) - max(s1[1], s2[1]))
        overlap_z = max(0, min(e1[2], e2[2]) - max(s1[2], s2[2]))

        # If there is an overlap in all dimensions, calculate the volume
        if overlap_x > 0 and overlap_y > 0 and overlap_z > 0:
            overlaps.append(overlap_x * overlap_y * overlap_z)

    return sum(overlaps)

# Example usage
x1 = np.array([[1, 0, 1], [2, 2, 2]])
x2 = np.array([[0, 0, 2], [2, 0, 2]])
print(overlap([x1], [x2]))


