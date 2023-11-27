import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, field, color):
    visited[x][y] = True
    for i in range(4):
        side_x = x + dx[i]
        side_y = y + dy[i]
        if (0 <= side_x < N) and (0 <= side_y < N) and not visited[side_x][side_y] and field[side_x][side_y] == color:
            dfs(side_x, side_y, field, color)

N = int(input())
field = [list(input().strip())for _ in range(N)]
field_2 = [[col.replace('G', 'R') for col in row] for row in field]

color = 0
person = 0

visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, field, field[i][j])
            person += 1

visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, field_2, field_2[i][j])
            color += 1

print(person, color)