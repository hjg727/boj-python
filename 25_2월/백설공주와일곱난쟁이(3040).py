"""import itertools

small = []

for _ in range(9):
    small.append(int(input()))

ans = itertools.combinations(small, 7)
res = set()
for i in ans:
    if sum(i) == 100:
        res.add(i)

for i in res:
    for res in i:
        print(res)"""

"""import itertools

dwarfs = [int(input()) for _ in range(9)]

for comb in itertools.combinations(dwarfs, 7):
    if sum(comb) == 100:
        for num in sorted(comb):
            print(num)
        break"""


dwarfs = [int(input()) for _ in range(9)]

def dfs(start, selected):
    if len(selected) == 7:
        if sum(selected) == 100:
            selected.sort()
            for dwarf in selected:
                print(dwarf)
        return
    
    for i in range(start, 9):
        selected.append(dwarfs[i])
        dfs(i+1, selected)
        selected.pop()

dfs(0, [])
