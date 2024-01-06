from heapq import heappush, heappop

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q, size, distance, count = [], 2, 0, 0
    
def bfs(i, j):
    visit = [[0] * n for _ in range(n)]
    heap = []
    heappush(heap, [0, i, j])#list자료형에 heap자료구조를 적용 
    visit[i][j] = 1
    while heap:
        d, x, y = heappop(heap)
        if 0 < field[x][y] < size:#갈 수 있는 곳으로    움직이기전 그리고 움직이고난 이후, 그 자리에 먹을 수 있는 물고기 찾음
            field[x][y] = 0
            return d, x, y
        for i in range(4):#일단 돌아다녀
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:#범위처리
                continue
            if not visit[nx][ny] and field[nx][ny] <= size:#방문안하고 사이즈가 작거나 같은 곳 찾으면 거기로 가고 방문처리해놓기
                visit[nx][ny] = 1
                heappush(heap, [d+1, nx, ny])#거리 1칸 올리고 다음좌표들을 올려준다.

    return -1, -1, -1

for i in range(n):
    for j in range(n):
        if field[i][j] == 9:#크기를가져오고 빈칸으로 만들기
            field[i][j] = 0
            q.append([i, j])

while q:
    q.sort()
    x, y = q.pop(0)
    d, nx, ny = bfs(x, y)
    if nx == -1:
        break
    q.append([nx, ny])
    distance += d
    count += 1
    if count == size:
        size += 1
        count = 0

print(distance)

"""
1. 아기 상어의 시작 위치를 찾습니다.
2. BFS를 사용하여 아기 상어가 이동할 수 있는 모든 위치를 찾습니다. 각 위치까지의 거리를 저장합니다.
3. 아기 상어보다 크기가 작은 물고기만을 대상으로 가장 가까운 물고기를 찾습니다. 만약 거리가 동일한 물고기가 여러 마리라면, 
   가장 위에 있는 물고기를 선택하고, 그런 물고기가 여러 마리라면 가장 왼쪽에 있는 물고기를 선택합니다.
4. 선택한 물고기를 먹고, 그 위치로 이동합니다. 이동 시간을 누적합니다.
5. 물고기를 먹은 횟수가 아기 상어의 크기와 동일하면 아기 상어의 크기를 1 증가시키고, 물고기를 먹은 횟수를 0으로 초기화합니다.
더 이상 먹을 수 있는 물고기가 없을 때까지 2번부터 5번까지의 과정을 반복합니다.
더 이상 먹을 수 있는 물고기가 없으면 누적된 이동 시간을 출력합니다.
"""