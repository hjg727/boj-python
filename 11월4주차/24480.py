import sys
sys.setrecursionlimit(10**6)
#재귀 제한 늘리는거 중요
input = sys. stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
tmp = 1

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



for i in range(1, len(graph)):
    graph[i].sort(reverse=True)
# sort는 None 반환 기억하기
# graph = [sorted(graph[i], reverse=True) for i in range(1, len(graph))]

def dfs(graph, visited, R):
    global tmp
    visited[R] = tmp
    tmp += 1
    for i in graph[R]:
        if visited[i] == 0:
            dfs(graph, visited, i)

dfs(graph, visited, R)

for i in range(1, N+1):
    print(visited[i] if visited[i] != 0 else 0)