from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(queue):
    day = 0
    while queue:
        x, y, day = queue.popleft()
        for i in range(4):
            side_x, side_y = x+dx[i], y+dy[i]
            if side_x<0 or side_x >= N or side_y < 0 or side_y >= M:
                continue
            if box[side_x][side_y] == 0 and visited[side_x][side_y] == False:
                queue.append((side_x, side_y, day+1))
                visited[side_x][side_y] = True
                box[side_x][side_y] = 1
    return day

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1 and visited[i][j] == False:
            queue.append((i, j, 0))
            #1인곳은 방문처리!
            visited[i][j] = True

day = bfs(queue)

if any(0 in row for row in box):
    print(-1)
else:
    print(day)
