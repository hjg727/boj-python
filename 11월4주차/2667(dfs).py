import sys
input = sys.stdin.readline

#상하좌우 좌표처리
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):#주변에 집있는 곳 찾기
    global count
    count += 1
    visited[x][y] = True
    for i in range(4):
        side_x, side_y = x + dx[i], y + dy[i]
        #인덱스 범위 처리
        if side_x < 0 or side_x >= N or side_y < 0 or side_y >= N:
            continue
        if field[side_x][side_y] == 1 and visited[side_x][side_y] == False:
            dfs(side_x, side_y)

N = int(input())
#sys썼을땐, strip()을 까먹지말기
field = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
ans = []#단지내의 집의 수

for i in range(N):
    for j in range(N):
        #탐색 도중 "여태 발견되지 않은" 집을 발견.
        if field[i][j] == 1 and visited[i][j] == False:
            count = 0
            dfs(i, j)#주변 탐색 시작
            ans.append(count)

print(len(ans))
for i in sorted(ans):
    print(i)