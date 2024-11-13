
input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

input = open("input.txt", "r").read()

X = input.splitlines()

res = []

cardstack1 = []
res = 0

from collections import defaultdict
d = defaultdict(list)
for c in X:
    card, x = c.split(":")
    cardn = int(card.split()[-1])
    d[cardn].append(c)

from tqdm import tqdm
for i in tqdm(range(len(X))):
    for x in d[i]:
        card, x = x.split(":")
        cardn = int(card.split()[-1])
        wc, mc = x.split("|")
        wc = list(map(int, wc.strip().split()))
        mc = list(map(int, mc.strip().split()))
        t = [x for x in mc if x in wc]
        if not t: continue
        for ind in range(cardn+1, cardn+1+len(t)):
            d[ind].append(X[ind-1])
    
r = 0
for k,v in d.items():
    print(k, len(v))
    r += len(v)


print(r)