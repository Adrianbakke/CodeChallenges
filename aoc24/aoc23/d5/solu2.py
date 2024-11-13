# dest rang start, source rang start, range length
input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split("\n\n")


#input = open("input.txt", "r").read().split("\n\n")

x = list(map(int, input[0].split(":")[-1].split()))
seeds = [(x[i],x[i+1]) for i in range(0,len(x),2)]

t = seeds
print(t)
maps = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

A,S,D,F = False,False,False,False
def map2(sstart, sle, s, l, d):
    splits = []
    end = sstart+sle

    # only end side inside map
    if s <= end < s+l and sstart < s:
       # splits.append((sstart, s-sstart))
        splits.append((d, end-s))
    
    # both side inside map
    elif s <= sstart < s+l and s <= end < s+l:
        splits.append((d+(sstart-s), sle))
    
    # only start inside
    elif s <= sstart < s+l and end >= s+l:
        splits.append(((sstart-s)+d, (s+l)-sstart))

    # both outside map
    elif sstart < s and end >= s+l:
        #splits.append((sstart, s-sstart))
        splits.append((d, l))
        #splits.append((s+l, end-(s+l)))

    return splits

from collections import defaultdict
from tqdm import tqdm
for c,x in tqdm(enumerate(input[1:])):
    x = x.splitlines()
    di = defaultdict(list)
    print(maps[c])
    for xx in x[1:]:
        d,s,l = map(int, xx.split())
        for tt in t:
            sstart, sle = tt
            splits = map2(sstart, sle, s, l, d)
            di[tt].extend(splits)


    for k,v in di.items():
        print(v)
        if not v:
            di[k] = [k]

    t = set([x for v in di.values() for x in v])
   #print(t)
    #exit()

#print(t)
vals = [x[0] for x in t]
print(sorted(vals)[:10])
