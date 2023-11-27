#유기농 배추
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            side_x, side_y = x+dx[i], y+dy[i]
            if side_x < 0 or side_x >=N or side_y < 0 or side_y>=M:#side_x>=M으로 한 실수 고치기
                continue
            if field[side_x][side_y] == 1 and visited[side_x][side_y] == False:
                queue.append((side_x,side_y))
                visited[side_x][side_y] = True
t = int(input())
ans = []
for _ in range(t):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    count = 0
    
    for _ in range(K):
        Y, X = map(int, input().split())#문제 함정 피하기
        field[X][Y] = 1
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                count += 1
    ans.append(count)
for i in range(t):
    print(ans[i])