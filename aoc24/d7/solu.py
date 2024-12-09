X = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()

X = open("input.txt","r").read().splitlines()

def rec(x, n=5, res=[]) -> list:
    if len(x)==n:
        res.append(x)
        return res
    rec(x+"*", n=n, res=res)
    rec(x+"+", n=n, res=res)
    rec(x+"|", n=n, res=res)
    return res

res=[]
for c,x in enumerate(X):
    print(c,"/",len(X), end="\r")
    ans, nums = x.split(": ")
    nums = nums.split(" ")
    combs = rec("",n=len(nums)-1, res=[])
    evals = nums[0]
    for c in combs:
        evals = nums[0]
        for n,o in zip(nums[1:],c):
            if o == "|":
                evals = str(evals) + n
            else:
                evals = eval(str(evals)+o+n)

        if eval(str(evals)) == int(ans):
            res.append(int(ans))
            break

print(sum(res))

