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

graph = [sorted(i) for i in graph]

def dfs(graph, visited, R):
    global tmp#전역변수로 선언해주는 이유 : 전체 방문 순서를 고려
    visited[R] = tmp
    tmp += 1
    for i in graph[R]:
        if visited[i] == 0:
            dfs(graph, visited, i)

dfs(graph, visited, R)

for i in range(1, N+1):
    print(visited[i] if visited[i] != 0 else 0)

#시간초과.. sys.stdin.readline;;