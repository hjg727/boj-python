from collections import deque


N, K = map(int, input().split())

res = 0

queue = deque([N])
visited = [0] * 100001
visited[N] = 1

while queue:
    current = queue.popleft()


    if current == K:
        res = visited[current] - 1
    
    for nx in (current-1,current+1,current*2):
        if 0 <= nx < 100_001 and not visited[nx]:
            visited[nx] = visited[current] + 1
            queue.append(nx)

print(res)