from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

def bfs(start):
    queue = deque([start])
    global count #방문 순서 업데이트
    visited[start] = count
    count += 1
    while queue:
        a = queue.popleft()
        
        for i in graph[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = count
                count += 1

bfs(R)

for i in range(1, N+1):
    print(visited[i])