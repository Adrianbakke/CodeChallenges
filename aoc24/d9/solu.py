
X = open("input.txt", "r").read()
X = "2333133121414131402"

# files = {0:int(X[0])}
# files.update({i-1:int(X[i]) for i in range(2,len(X), 2)})
files = [int(X[i]) for i in range(0,len(X), 2)]
space = [int(X[i]) for i in range(1,len(X), 2)]
print(space)


res = 0
L = len(files)
p = 0
k = 1
j = 0
i = 0
while i < len(space)-1:

    for fv in range(files[j]):
        res += j*p
        print(j,p, i, L-k)
        p += 1

    j += 1
    lv = L-k
    while space[i]:# and lv>i:
        files[lv] -= 1
        space[i] -= 1
        res += lv*p
        p += 1
        if space[i] == 0:
            if files[lv] == 0: 
                k += 1
                lv = L-k
            break
        if files[lv] == 0: 
            k += 1
            lv = L-k

    #if lv<i:
    #    break
    i += 1
    

print(res)


        

        


