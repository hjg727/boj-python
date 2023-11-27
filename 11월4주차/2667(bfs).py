from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])#좌표를 튜플로 처리
    visited[x][y] = True
    count = 1
    while queue:
        x, y = queue.popleft()#튜플 처리 덕분에 각각의 좌표 얻기 성공
        for i in range(4):
            side_x, side_y = x + dx[i], y + dy[i]
            if side_x<0 or side_x>=N or side_y<0 or side_y>=N:
                continue
            if field[side_x][side_y] == 1 and visited[side_x][side_y] == False:
                queue.append((side_x, side_y))#튜플로 append하기
                visited[side_x][side_y] = True #방문 처리
                count += 1
    return count

N = int(input())
field = [list(map(int, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if field[i][j] == 1 and visited[i][j] ==False:
            ans.append(bfs(i, j))
print(len(ans))
for i in sorted(ans):
    print(i)