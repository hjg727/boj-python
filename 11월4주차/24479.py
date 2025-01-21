N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)] #각 정점과 간선 정보 받을 그래프
visited = [0] * (N+1) #방문 기록
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = [sorted(i) for i in graph]

def dfs(R):
    visited[R] = 1
    print(R)
    for i in graph[R]:
        if not visited[i]:
            dfs(i)

dfs(R)

#엥 뭔가이상하다. 런타임에러가 뜬다..
#i번째 줄에는 정점 i의 방문 순서를 출력한다.헉 이거 신경 안썼다...
#이게 어떻게 틀렸다라고 안뜬거지..
#출력부분도 오류인 것 같다.
