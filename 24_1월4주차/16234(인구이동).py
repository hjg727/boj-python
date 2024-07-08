from collections import deque
import sys
input = sys.stdin.readline
N, L, R = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(x, y):
    global moved
    group = [(x,y)]
    visited[x][y] = united #연합 번호
    population = field[x][y] #시작 인구
    extents = 1 #범위
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if L <= abs(field[nx][ny] - field[x][y]) <= R:
                    q.append((nx, ny))
                    visited[nx][ny] = united
                    extents += 1
                    population += field[nx][ny]
                    group.append((nx,ny))
        
    for a, b in group:
        field[a][b] = population // extents
        
    if extents > 1:
        moved = True

day = 0

while True:
    moved = False
    visited = [[-1] * N for _ in range(N)]
    united = 0 #깃발 번호
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                bfs(i, j)
                united += 1

    if not moved:
        break

    day += 1
    
print(day)