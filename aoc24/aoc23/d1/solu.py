input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
input = open("input.txt", "r").read()


input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

input = open("input.txt", "r").read()
x = input.splitlines()
res = []

nums =  {"one": 1, "two": 2, "three":3 , "four": 4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

numlist =[]
for k,v in nums.items():
    for kk,vv in nums.items():
        if k[-1] == kk[0]:
            numlist.append([k + kk[1:],int(str(v)+str(vv))])

for k,v in nums.items():
    numlist.append([k,v])

for xx in x:
    print(xx)
    for k,v in numlist:
        xx = xx.replace(k, str(v))
    print(xx)
    print()
    nums = "".join(z for z in xx if z.isnumeric())
    rn = nums[0] + nums[-1]
    res.append(int(rn))

print(sum(res))