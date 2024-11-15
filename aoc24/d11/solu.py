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

from dataclasses import dataclass
@dataclass
class NumTracker:
   p: int
   m: list

@dataclass
class Monkey:
    id: int
    opt: str
    items: list[NumTracker]
    test: list
    # nt: NumTracker
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

for round in range(1000):
  print(round)
  for m in mnkys:
      for _ in range(len(m.items)):
        m.insp += 1
        insp = m.items.pop(0)
        wlvl = eval(m.opt.split("=")[1].strip().replace("old", str(insp))) # //3
        test = 1 if wlvl%int(m.test[0].split(" ")[-1])==0 else 2
        nxtm = int(m.test[test].split(" ")[-1])
        mnkys[nxtm].items.append(wlvl)
        #print(insp, wlvl, test, nxtm)

for m in mnkys:
   print(m.insp) 
    