from collections import deque
import copy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(): #일단 전염병 퍼지는 로직
    queue = deque()

    t_field = copy.deepcopy(field) #검색으로 찾은 깊은복사

    for i in range(N):
        for j in range(M):
            if t_field[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and t_field[nx][ny] == 0:
                t_field[nx][ny] = 2
                queue.append((nx, ny))
    
    global result#퍼지고 난 다음 전체 안전구역 검사
    count = 0
    for i in range(N):
        for j in range(M):
            if t_field[i][j] == 0:
                count += 1
    
    result = max(result, count)#모든 경우의 수 중, 가장 많은 안전구역 확보한 케이스 저장

def wall(count):#벽 세우는 로직, 백트래킹 개념.. 어려웠다..
    if count == 3:#벽을 다 세운 상태에서 전염 시작
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:#맵 전체 0중 하나씩 들어가서 1만들고 돌아와서 리셋 기능
                field[i][j] = 1
                wall(count + 1)
                field[i][j] = 0

wall(0)#벽을 안세웠으니, 0 start

print(result)

