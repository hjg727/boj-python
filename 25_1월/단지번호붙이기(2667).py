"""Sudo
N 입력받기
N*N크기의 필드 초기 설정
N*N크기의 방문 필드 초기 설정

상하좌우 이동을 위한 dx, dy

bfs함수:
x, y 좌표와 방문필드를 매개변수 받아서
해당 위치의 방문처리
단지의 갯수 초기설정
FIFO 로직에 맞게 큐 자료구조 활용
큐가 안비어있을동안
시작점에서 상하좌우 방문처리하기 (조건: 아직 방문하지 않은 곳 + 단지가 있는곳(1))

전체 필드 조회 이중for문
만약 방문하지않았고 단지가 있는 곳이라면 bfs함수 호출
"""

from collections import deque

N = int(input())
field=[]
#입력 받기
for _ in range(N):
    a = list(map(int, input().rstrip()))
    field.append(a)
visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and field[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                count += 1
    
    return count

ans = []

for i in range(N):
    for j in range(N):
        if field[i][j] and not visited[i][j]:
            ans.append(bfs(i, j, visited))

print(len(ans))
ans.sort()
for i in ans:
    print(i)