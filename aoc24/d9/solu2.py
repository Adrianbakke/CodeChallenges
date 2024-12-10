
X = open("input.txt", "r").read()
#X = "2333133121414131402"

sind = 0
eind = 0
f = []
s = []
k = 0
for i in range(len(X)):
    if i%2==0:
        sind = eind 
        eind = sind + int(X[i])
        f.append([[sind,eind], k])
        k += 1
    else:
        sind = eind 
        eind = sind + int(X[i])
        s.append([sind,eind])

for fi in range(len(f)):
    for si in range(len(s)):
        if f[len(f)-fi-1][0][0]<=s[si][0]: break
        lv = f[len(f)-fi-1][0][1] - f[len(f)-fi-1][0][0]
        ls = s[si][1] - s[si][0]
        if lv==ls:
            ss,e = s.pop(si)
            f[len(f)-fi-1][0][0] = ss
            f[len(f)-fi-1][0][1] = e
            g = 1
            break
        if 0<lv<ls:
            t = s[si][0] 
            f[len(f)-fi-1][0][0] = t
            f[len(f)-fi-1][0][1] = t+lv
            s[si][0] += lv
            g = 1
            break

res = 0
for (s,e),v in f:
    for i in range(s,e):
        res += i*v

print(res)
