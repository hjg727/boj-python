from collections import deque
import copy

N, M = map(int, input().split())

field = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

ans = 0

def bfs():
    queue = deque(virus)

    t_field = copy.deepcopy(field)
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and t_field[nx][ny] == 0:
                t_field[nx][ny] = 2
                queue.append((nx, ny))
    global ans
    count = sum(i.count(0) for i in t_field)
    ans = max(ans, count)


def wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                field[i][j] = 1
                wall(count + 1)
                field[i][j] = 0

virus = [(i,j) for i in range(N) for j in range(M) if field[i][j] == 2]
wall(0)

print(ans)