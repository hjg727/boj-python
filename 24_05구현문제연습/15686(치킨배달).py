from itertools import combinations

def direct(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            house.append((i, j))
        elif field[i][j] == 2:
            chicken.append((i, j))
candidate = list(combinations(chicken, M))
def get_sum(candidate):

    res = 0
    # (모든) 집의 위치에대하여
    for hx, hy in house:
        temp = 1e9
        #골라진 치킨집 위치와의 최소 거리
        for cx, cy in candidate:
            temp = min(temp, direct(hx, hy, cx, cy))
        #res는 1번 집위치에대한 골라진 치킨집 위치와의 최소거리 + 2번집~~+3번집~~+n번집~~
        res += temp
    
    return res

result = 1e9

for candidate in candidate:
    result = min(result, get_sum(candidate))

print(result)