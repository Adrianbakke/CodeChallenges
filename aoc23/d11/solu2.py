input = """Monkey 0:
  Starting items: 62, 92, 50, 63, 62, 93, 73, 50
  Operation: new = old * 7
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 1

Monkey 1:
  Starting items: 51, 97, 74, 84, 99
  Operation: new = old + 3
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 4

Monkey 2:
  Starting items: 98, 86, 62, 76, 51, 81, 95
  Operation: new = old + 4
  Test: divisible by 13
    If true: throw to monkey 5
    If false: throw to monkey 4

Monkey 3:
  Starting items: 53, 95, 50, 85, 83, 72
  Operation: new = old + 5
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 0

Monkey 4:
  Starting items: 59, 60, 63, 71
  Operation: new = old * 5
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 5:
  Starting items: 92, 65
  Operation: new = old * old
  Test: divisible by 5
    If true: throw to monkey 6
    If false: throw to monkey 3

Monkey 6:
  Starting items: 78
  Operation: new = old + 8
  Test: divisible by 3
    If true: throw to monkey 0
    If false: throw to monkey 7

Monkey 7:
  Starting items: 84, 93, 54
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 1
""".split("\n\n")

#input = """Monkey 0:
#Starting items: 79, 98
#Operation: new = old * 19
#Test: divisible by 23
  #If true: throw to monkey 2
  #If false: throw to monkey 3
#Monkey 1:
#Starting items: 54, 65, 75, 74
#Operation: new = old + 6
#Test: divisible by 19
  #If true: throw to monkey 2
  #If false: throw to monkey 0
#Monkey 2:
#Starting items: 79, 60, 97
#Operation: new = old * old
#Test: divisible by 13
  #If true: throw to monkey 1
  #If false: throw to monkey 3
#Monkey 3:
#Starting items: 74
#Operation: new = old + 3
#Test: divisible by 17
  #If true: throw to monkey 0
  #If false: throw to monkey 1#""".split("\n\n")

from dataclasses import dataclass, field
from functools import reduce


@dataclass
class NumLazy:
  realized: bool = True
  p: int = 0
  m: list = field(default_factory=list)
  def add(self, op, n):
    if op == "+":
      mm = reduce(lambda x,y: x*y, self.m, 1)
      self.p = (self.p*mm)+int(n)
      self.realized,self.m = True,[]
    elif op == "*":
      self.realized = False
      if n == "old":
          pass
          #self.m.extend(self.m)
          #self.m.append(self.p)
      else: self.m.append(int(n))
    else: raise Exception("illegal operator")

@dataclass
class Monkey:
    id: int
    opt: str
    items: list[NumLazy]
    test: list
    insp: int = 0

mnkys = []
for i in input:
    dat = {"id": None, "items": None, "opt": None, "test": []}
    for e in i.splitlines():
        x = e.split(":")
        typ = x[0].strip()
        if   typ == "Starting items": dat["items"] = [int(xx) for xx in x[1].strip().split(", ")]
        elif typ == "Operation":      dat["opt"] = x[1].strip()
        elif typ == "Test":           dat["test"].append(x[1].strip())
        elif typ == "If false":       dat["test"].append(x[1].strip())
        elif typ == "If true":        dat["test"].append(x[1].strip())
        else: dat["id"] = int(x[0].split(" ")[1])
    mnkys.append(Monkey(**dat))

import math
lcd = math.prod([int(m.test[0].split(" ")[-1]) for m in mnkys])

for round in range(10_000):
  for m in mnkys:
    for _ in range(len(m.items)):
      m.insp += 1
      itm = m.items.pop(0)
      itm = itm%lcd
      op, n = m.opt.split("=")[1].strip().split(" ")[1:]
      itm = eval(m.opt.split("=")[1].strip().replace("old", str(itm))) # //3
      testn = int(m.test[0].split(" ")[-1])
      test = 1 if itm%testn==0 else 2
      nxtm = int(m.test[test].split(" ")[-1])
      mnkys[nxtm].items.append(itm)
res = []
for m in mnkys:
   res.append(m.insp) 
print(sorted(res))
    