import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        side_x, side_y = x + dx[i], y + dy[i]
        if side_x < 0 or side_x >= N or side_y < 0 or side_y >=N:
            continue
        if field[side_x][side_y] == 1 and visited[side_x][side_y] == False:
            dfs(side_x,side_y)
N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]

ans = []

#2차원배열의 최소, 최대 찾기
min_height, max_height = min(map(min, height)), max(map(max, height))

for i in range(min_height-1, max_height):
    #max_height+1이 아닌이유 장마의 높이가 max_height이면 다 잠겨서 구할 가치가 없음
    count = 0
    field = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if height[a][b] > i:
                field[a][b] = 1
    for x in range(N):
        for y in range(N):
            if field[x][y] == 1 and visited[x][y] == False:
                dfs(x,y)
                count += 1
    ans.append(count)
print(max(ans))