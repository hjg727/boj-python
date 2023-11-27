from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, V = map(int, input().split())
#N: 정점의 개수, M: 간선의 개수, V: 시작 정점

graph = [[] for _ in range(N+1)]#각 정점의 간선 정보담을 리스트
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

#dfs구현
def DFS(start):
    print(start, end = ' ')
    visited_dfs[start] = start
    for i in graph[start]:
        if visited_dfs[i] == 0:
            DFS(i)

#bfs구현
def BFS(start):
    queue = deque([start])
    
    visited_bfs[start] = start
    print(start, end = ' ')
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = i
                print(i, end = ' ')



DFS(V)
print()#줄 바꿈
BFS(V)