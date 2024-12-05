X = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
X = open('input.txt', 'r').read()
X = X.split("\n\n")

rules = list(map(lambda x: list(map(int, x.split("|"))), X[0].splitlines()))
update = list(map(lambda x: list(map(int, x.split(','))), X[1].splitlines()))

res = []
for i in range(len(update)):
    ok = False
    u = update[i]
    j = 0
    while j<len(rules):
        r = rules[j]
        try:
            indf,inds = u.index(r[0]), u.index(r[1])
            if indf < inds:
                j+=1
            else:
                t = u[indf]
                u[indf] = u[inds]
                u[inds] = t
                ok = True
                j=0
        except:
            j+=1

    if ok: 
        print(u)
        res.append(u[len(u)//2])

print("ANSWER:")
print(sum(res))
