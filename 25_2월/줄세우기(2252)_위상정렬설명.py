"""
리스트 안에 
b가 있을 때 
없을때

a가 있을 때 b가 있으면 b앞에 배치 b가 없으면 ans.append(a) 하고 ans.append(b)하기
없을 때 b가 있으면 b 앞에 배치 b가 없으면 ans.append(a) 하고 ans.append(b) 하기
"""
"""첫번째 풀이
N, M = map(int, input().split())

man = [range(1, N+1)]
ans = []

for _ in range(M):
    a, b= map(int, input().split()) # A가 B앞에 서야된다.
    
    # if b in ans:
    #     i = ans.index(b)
    #     ans.insert(i, a)
    #     continue
    
    if a in ans:
        i = ans.index(a)
        a = ans.pop(i)
        if b in ans:
            j = ans.index(b)
            ans.insert(j, a)
        else:
            ans.append(a)
            ans.append(b)
    else:
        if b in ans:
            j = ans.index(b)
            ans.insert(j, a)
        else:
            ans.append(a)
            ans.append(b)


print(" ".join(map(str, ans)))"""
import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
stack = []

# 간선 정보 입력받기
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# DFS 함수
def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
    stack.append(node)  # 모든 인접 노드 방문 후 스택에 추가

# 위상 정렬 실행
def topological_sort():
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
    
    stack.reverse()  # 스택을 뒤집어서 출력
    print(" ".join(map(str, stack)))

topological_sort()



"""
위상 정렬을 이해하려면 그래프 이론의 기본 개념을 알고 있어야 해!
아래 개념들을 먼저 익히면 위상 정렬을 더 쉽게 이해할 수 있어.

1️⃣ 그래프(Graph)란?
	•	여러 개의 노드(정점, Vertex) 와 간선(Edge) 으로 이루어진 자료구조.
	•	노드(Node, Vertex): 데이터를 담고 있는 점.
	•	간선(Edge): 노드 간의 관계를 나타내는 선.

📌 예제 (노드 1~5가 있고, 간선이 연결된 그래프)

1 → 2 → 5  
↓    ↓  
3 → 4  

이 그래프는 다음과 같이 표현 가능:

graph = {
    1: [2, 3],
    2: [5, 4],
    3: [4],
    4: [],
    5: []
}

2️⃣ 방향 그래프 vs 무방향 그래프
	•	방향 그래프 (Directed Graph): 간선에 방향이 있음. (예: 1 → 2)
	•	무방향 그래프 (Undirected Graph): 간선이 양방향. (예: 1 - 2)

📌 위상 정렬은 반드시 방향 그래프에서만 사용 가능!
(방향이 없는 그래프에서는 순서를 정하는 개념이 성립하지 않음.)

3️⃣ 사이클(Cycle) 없는 그래프 (DAG)

위상 정렬이 동작하려면 DAG(Directed Acyclic Graph) 여야 해!
	•	DAG: 방향 그래프면서 사이클이 없는 그래프
	•	만약 그래프에 사이클이 있으면 위상 정렬 불가능

📌 사이클 예시 (위상 정렬 불가능!)

1 → 2 → 3  
↑       ↓  
5 ← 4  

	•	1 → 2 → 3 → 4 → 5 → 1로 순환(사이클) 이 있어서 위상 정렬 불가능!

📌 DAG 예시 (위상 정렬 가능!)

1 → 2 → 3  
↓    ↓  
4    5  

	•	사이클이 없어서 위상 정렬 가능!

4️⃣ 진입 차수 (Indegree)
	•	진입 차수란 한 노드로 들어오는 간선의 개수
	•	위상 정렬에서는 진입 차수가 0인 노드를 먼저 처리

📌 예제:

1 → 2 → 3  
↓    ↓  
4    5  

진입 차수 구하기:
	•	1: 0 (들어오는 간선 없음)
	•	2: 1 (1 → 2)
	•	3: 1 (2 → 3)
	•	4: 1 (1 → 4)
	•	5: 1 (2 → 5)

위상 정렬은 항상 진입 차수가 0인 노드부터 처리!

📌 정리: 위상 정렬을 이해하려면?

✅ 그래프 개념 (노드, 간선)
✅ 방향 그래프 vs 무방향 그래프 차이
✅ 사이클이 없는 그래프 (DAG)
✅ 진입 차수 (Indegree) 개념

이걸 이해하면 위상 정렬이 훨씬 쉽게 다가올 거야!
그래도 헷갈리면 질문해줘 😊

위상 정렬을 간단한 코드로 설명해볼게!
위상 정렬을 구현하는 대표적인 방법 두 가지를 코드로 보여줄게.

1️⃣ 진입 차수를 이용한 위상 정렬 (Kahn’s Algorithm)

아이디어:
	•	진입 차수(indegree, 들어오는 간선의 개수)가 0인 노드를 먼저 처리한다.
	•	그 노드와 연결된 간선을 제거하고, 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.
	•	이를 반복하면 정렬된 순서가 나온다.

from collections import deque

# 그래프 입력 받기
N, M = map(int, input().split())  # 노드 개수 N, 간선 개수 M
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

# 간선 정보 입력받기
for _ in range(M):
    A, B = map(int, input().split())  # A가 B보다 먼저 와야 함
    graph[A].append(B)
    indegree[B] += 1  # B의 진입 차수 증가

# 위상 정렬 실행
def topological_sort():
    result = []  # 정렬된 결과 저장
    q = deque()

    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        # 현재 노드와 연결된 노드들의 진입 차수 감소
        for next_node in graph[now]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)

    print(" ".join(map(str, result)))

topological_sort()

📌 시간복잡도:
	•	모든 간선을 한 번씩 탐색 → O(N + M)
	•	큐를 사용해서 빠르게 정렬 가능

2️⃣ DFS를 이용한 위상 정렬

아이디어:
	•	방문하지 않은 노드에서 DFS를 수행
	•	재귀 호출이 끝나면 스택에 노드를 추가
	•	스택을 뒤집어서 위상 정렬 결과를 얻음

import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
stack = []

# 간선 정보 입력받기
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# DFS 함수
def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
    stack.append(node)  # 모든 인접 노드 방문 후 스택에 추가

# 위상 정렬 실행
def topological_sort():
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
    
    stack.reverse()  # 스택을 뒤집어서 출력
    print(" ".join(map(str, stack)))

topological_sort()

📌 시간복잡도:
	•	모든 노드를 한 번 방문하면서 탐색 → O(N + M)

✅ 어떤 방법을 선택해야 할까?
	•	큐(BFS 방식, Kahn’s Algorithm) → 더 직관적이고, 코드가 간결해서 실전에서 더 자주 사용됨
	•	DFS 방식 → 재귀를 사용할 수 있을 때 유용하며, 스택을 활용한 접근이 필요할 때 사용됨

위상 정렬 이해됐어? 더 궁금한 거 있으면 질문해줘! 😊
"""