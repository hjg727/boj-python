import itertools
N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

def distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            house.append((i,j))
        elif field[i][j] == 2:
            chicken.append((i,j))

pick_chicken = list(itertools.combinations(chicken, M))

res = 1e9
for pick in pick_chicken:
    city_distance = 0
    for x1, y1 in house:
        temp = 1e9
        for x2, y2 in pick:
            temp = min(temp, distance(x1,y1,x2,y2))

        city_distance += temp
    res = min(res, city_distance)
print(res)