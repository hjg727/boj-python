#유기농 배추
#상하좌우나온다? 바로 dx,dy
import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        side_x, side_y = x+dx[i], y+dy[i]
        if side_x < 0 or side_x >=N or side_y < 0 or side_y>=M:#side_x>=M으로 한 실수 고치기
            continue
        if field[side_x][side_y] == 1 and visited[side_x][side_y] == False:
            dfs(side_x,side_y)

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
                dfs(i, j)
                count += 1
    ans.append(count)
for i in range(t):
    print(ans[i])