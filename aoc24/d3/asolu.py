from functools import reduce

X = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
X = open("input.txt", "r").read()

def filter_mult(seq):
    cmp = "mul("
    dont = "don't()"
    do = "do()"
    active = True
    muls = []
    i = 0
    while i < len(seq):
        if seq[i:i+len(dont)] == dont:
            active = False
            i+=len(dont)
        if seq[i:i+len(do)] == do:
            active = True
            i+=len(do)
        if seq[i:i+len(cmp)] == cmp and active:
            i += len(cmp)
            t = i
            fake = False
            while seq[i] != ")":
                print(seq[i], seq[i] != "," and (not seq[i].isnumeric()))
                if seq[i] != "," and not seq[i].isnumeric():
                    fake = True
                    break
                i += 1
            if not fake:
                muls.append(list(map(int, seq[t:i].split(","))))
        else:
            i+=1
    return muls


l = filter_mult(X)
result = sum(reduce(lambda x, y: x * y, pair) for pair in l)
print(result)
