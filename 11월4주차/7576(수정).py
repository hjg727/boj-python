from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    while queue:
        x, y, day = queue.popleft()
        for i in range(4):
            side_x, side_y = x+dx[i], y+dy[i]
            if side_x<0 or side_x >= N or side_y < 0 or side_y >= M:
                continue
            if box[side_x][side_y] == 0 and visited[side_x][side_y] == False:
                queue.append((side_x, side_y, day+1))#다음날 한번 더 상하좌우 탐색
                visited[side_x][side_y] = True#방문 처리
                box[side_x][side_y] = 1 #익은과일 처리 안함
    return day

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

ans = []
#수정할 부분: 일단 전체 탐색하고 익어있는 과일들의 위치를 받아야된다.
for i in range(N):
    for j in range(M):
        if box[i][j] == 1 and visited[i][j] == False:
            ans.append(bfs(i, j))
            visited[i][j] = True


if any(0 in row for row in box):
    print(-1)
else:
    print(max(ans))