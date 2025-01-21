from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    #global day#잘못된 day처리
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()#O(1)
        for i in range(4):
            side_x, side_y = x+dx[i], y+dy[i]
            if side_x<0 or side_x >= N or side_y < 0 or side_y >= M:
                continue
            if box[side_x][side_y] == 0 and visited[side_x][side_y] == False:
                queue.append((side_x, side_y))
                visited[side_x][side_y] = True #방문 처리
                #box[side_x][side_y] = 1 익은과일 처리 안함
        day += 1#하루에 한번 상하좌우 탐색
    return day

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

day = 0

ans = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1 and visited[i][j] == False:
            ans.append(bfs(i, j))

if 0 not in box:#잘못된 출력방식
    print(ans)#..왜 값이 두 개가 뜨지..
else:
    print(-1)