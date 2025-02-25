from itertools import combinations

N = int(input())

food = []

for _ in range(N):
    s, b = map(int, input().split())
    food.append((s,b))

min_taste = 1e9

for i in range(1,N+1):
    for subset in combinations(food, i):
        sour = 1
        bitter = 0

        for s, b in subset:
            sour *= s
            bitter +=b
        
        total = abs(sour - bitter)

        min_taste = min(min_taste, total)

print(min_taste)



"""
from itertools import combinations

N = int(input())

food = []

for _ in range(N):
    s, b = map(int, input().split())
    food.append((s,b))

taste = []

for i in range(1,N+1):
    for subset in combinations(food, i):
        taste.append(list(subset))
res = 1e9

for comb in taste:
    print(comb
"""