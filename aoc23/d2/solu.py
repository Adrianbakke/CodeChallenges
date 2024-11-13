input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

input = open("input.txt", "r").read()
x = input.splitlines()
res = []


# 12 red cubes, 13 green cubes, and 14 blue cubes


rd = {"red": 12, "green": 13, "blue": 14}
ids = []
for xx in x:
    gameid, xx = xx.split(":")
    game = xx.split(";")
    f = True
    sv = {}
    for g in game:
        for gg in g.split(","):
            gg = gg.strip().split(" ")
            v, color = gg
            #if int(v) > rd[color]:
            #    f = False
            try:
                if int(v) > sv[color]:
                    sv[color] = int(v)
            except:
                sv[color] = int(v)

            
    #if f: ids.append(int(gameid.split(" ")[1]))
    ids.append(sv)

res = []
import math
for i in ids:
    print(i)
    a = math.prod(i.values())
    res.append(a)
    print(a)
print(sum(res))