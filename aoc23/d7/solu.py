test_input = f"""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

test_input.pop(0)

input = open("input.txt", "r").read().splitlines()
input.pop(0)

test_input = input

class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.child = []
        self.content = []
    def sz(self):
        res = sum([int(x[0]) for x in self.content])
        for c in self.child: res += c.sz()
        return res

cdir = Dir("/", None)
c1dir = cdir

ctnt = []
while len(test_input)>0:
    l = test_input.pop(0).split(" ")
    if l[0] == "$":
        ctnt = []
        if l[1] == "cd":
            if l[2] == "..":
                c1dir = c1dir.parent
            else:
                for c in c1dir.child:
                    if c.name == l[2]:
                        c1dir = c
                        break
        continue

    tp, name = l
    if tp == "dir":
        c1dir.child.append(Dir(name, c1dir))
    else:
        c1dir.content.append([tp, name])


NEEDED_SPACE = 30000000
USED_SPACE = 70000000 - cdir.sz()

res = []
def rec(d):
    sz = d.sz()
    # if sz <= 100000: res.append(sz) # solu1
    if USED_SPACE+sz >= NEEDED_SPACE: res.append(sz) # solu2
    if d.child:
        for c in d.child:
            rec(c)

rec(cdir)

print(res, min(res))
