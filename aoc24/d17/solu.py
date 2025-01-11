input = """Register A: 6617486
Register B: 0
Register C: 0

Program: 2,4,1,6,7,5,4,6,1,4,5,5,0,3,3,0"""

# input = """Register A: 729
# Register B: 0
# Register C: 0
#
# Program: 0,1,5,4,3,0"""

# input = """Register A: 2024
# Register B: 0
# Register C: 0
#
# Program: 0,3,5,4,3,0"""

regstmp, prog = input.split("\n\n")

regs = {}
for x in regstmp.split("\n"):
    reg,val = x.split(": ")
    regs[reg.split(" ")[-1]] = int(val) 

prog = list(map(int, prog.split(": ")[-1].split(",")))

ip = 0

def operand(x):
    mapping = {
        4: regs['A'],
        5: regs['B'],
        6: regs['C']
    }
    return mapping.get(x, x)

def run(best):
    output = []
    ip = 0
    oldA = regs['A']
    while ip < len(prog):
        inst = prog[ip]
        litop = prog[ip+1]
        combop = operand(litop)
        if inst == 0:
            num = regs['A']
            regs['A'] = num>>combop
            ip += 2
        elif inst == 1:
            regs['B'] = regs['B']^litop
            ip += 2
        elif inst == 2:
            regs['B'] = combop%8
            ip += 2
        elif inst == 3:
            if regs['A'] != 0:
                ip = litop
            else:
                ip += 2
        elif inst == 4:
            regs['B'] = regs['B']^regs['C']
            ip += 2
        elif inst == 5:
            output.append(combop%8)
            if output[len(output)-1]!=prog[len(output)-1]:
                if len(output) > best:
                    best = len(output)
                    print(output, oldA)
                break
            ip += 2
        elif inst == 6:
            num = regs['A']
            regs['B'] = num>>combop
            ip += 2
        elif inst == 7:
            num = regs['A']
            regs['C'] = num>>combop
            ip += 2
    return output,best



nott = regs['A']
outp = []
i = 0
a=0
best= 0
print(prog)
while not outp==prog:
    regs['A']=a
    regs['B']=0
    regs['C']=0
    outp,best = run(best)
    a = i*8**10+0o3435400351
    print(a)

    i+=1


print(regs)
