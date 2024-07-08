import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1) #한 정점으로 가기위한 걸리는 거리 리스트

for i in range(E):
    u, v, w = map(int, input().split())
    # v는 가야할 정점 w는 가중치
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))#자기 자신의 가중치 0, 현재 정점
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:# (2, 2), (3, 3)
            cost = dist + i[1]#총 비용 = 건너갈 가중치 + 저장된 가중치
            if cost < distance[i[0]]:#최소 비용 구하기 로직
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])