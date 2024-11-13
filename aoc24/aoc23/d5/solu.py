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

input = open("input.txt", "r").read().split("\n\n")

seeds = list(map(int, input[0].split(":")[-1].split()))

t = seeds

from tqdm import tqdm
for x in tqdm(input[1:]):
    x = x.splitlines()
    g = {}
    for xx in x[1:]:
        d,s,l = map(int, xx.split())
        #d,s = range(d, d+l), range(s, s+l)
        for tt in t:
            if s <= tt <= s+l:
                g[tt]=(tt-s)+d
                # g.update({y:x for x,y in zip(d,s) if y in t})
    for tt in t:
        if g.get(tt) is None:
            g[tt] = tt
    t = g.values()

print(g)
print(min(g.values()))
