from collections import deque

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(i, j):
    visited = [[False]*n for _ in range(n)]
    visited[i][j] = True
    eat = []#지나가다가 먹은것
    distance = [[0]*n for _ in range(n)]
    q = deque([(i, j)])#리스트형태의 덱
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if field[nx][ny] <= field[i][j] or field[nx][ny] == 0:#크기가 작거나 빈곳이면
                    q.append((nx, ny))#튜플로 넘기기
                    visited[nx][ny] = True#방문처리하고
                    distance[nx][ny] = distance[x][y] + 1#거리를 1올린다. 거리 = 시간
                if 0 < field[nx][ny] < field[i][j]:#만약 크기가 작고 빈곳이 아니라면
                    eat.append((distance[nx][ny], nx, ny))#먹는다.
    if not eat:#주변에 먹을게 없다면 -1
        return -1, -1, -1
    eat.sort()#튜플들을 sort하면 거리순 다음 x좌표순, 다음 y좌표순이다.
    return eat[0][0], eat[0][1], eat[0][2]

time = 0
eat = 0
for i in range(n):
    for j in range(n):
        if field[i][j] == 9:
            x, y = i, j
            field[i][j] = 2#아기상어의 위치를 x,y로 넘기고 그 위치의 값을 9에서 상어의 크기로 수정
while True:
    dist, nx, ny = bfs(x, y)#먹을곳 위치들을 받게 되면
    if nx == -1:
        break
    field[nx][ny] = field[x][y]#상어의 위치를 먹거나 지나간곳으로 업데이트
    field[x][y] = 0#상어가 있던 곳은 빈곳으로 처리
    
    x, y = nx, ny#다시 업데이트
    time += dist
    eat += 1
    if eat == field[x][y]:#상어의 크기 만큼 물고기를 먹었다면
        field[x][y] += 1
        eat = 0

print(time)

"""
이 코드는 아기 상어의 위치부터 BFS를 시작하여, 아기 상어가 갈 수 있는 위치를 큐에 추가하면서 물고기를 찾아가는 방식입니다. 
물고기를 찾으면 그 물고기까지의 거리와 위치를 리스트에 저장하고, 
물고기를 모두 찾은 후에는 거리가 가장 짧은 물고기를 먹습니다.(같다면, x좌표가 더 작고 그 담으로 y좌표가 더 작은 곳)
아기 상어가 물고기를 먹은 후에는 그 위치로 이동하고, 아기 상어가 물고기를 자신의 크기만큼 먹을 때마다 크기를 1 증가시킵니다. 
이 과정을 더 이상 먹을 물고기가 없을 때까지 반복하며, 아기 상어가 물고기를 찾아다니는 데 걸리는 시간을 누적하여 결과를 출력합니다.
"""