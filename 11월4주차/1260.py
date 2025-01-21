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
def DFS(graph,start):
    #이 부분이 문제다. 방문순서대로 정점번호를 넣은게 아니라, 
    #방문순서대로 정점번호인 인덱스에 정점번호를넣었다..
    visited_dfs[start] = start
    for i in graph[start]:
        if visited_dfs[i] == 0:
            DFS(graph, i)

#bfs구현
def BFS(graph, start):
    queue = deque([start])
    #이 부분이 문제다. 방문순서대로 정점번호를 넣은게 아니라, 
    #방문순서대로 정점번호인 인덱스에 정점번호를넣었다..
    visited_bfs[start] = start
    
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = i



DFS(graph, V)
BFS(graph, V)

print(' '.join(map(str,visited_dfs[1:])))
print(' '.join(map(str, visited_bfs[1:])))

#아니면 각각 밑과 같이 처리
"""
for i in visited[1:]:
    print(i + end(' '))
"""