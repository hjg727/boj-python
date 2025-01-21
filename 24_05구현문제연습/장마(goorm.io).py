N, M = map(int, input().split())

homes = list(map(int, input().split()))

prevRain = set()

for day in range(1, M+1):
    s, e = map(int, input().split())

    for i in range(s-1, e):
        homes[i] += 1
        prevRain.add(i)
    
    if day % 3 == 0:
        for i in prevRain:
            homes[i] -= 1
        
        prevRain.clear()

print(' '.join(map(str, homes)))