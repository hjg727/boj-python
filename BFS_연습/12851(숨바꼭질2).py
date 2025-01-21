from collections import deque


N, K = map(int, input().split())

queue = deque([N])
visited = [0]*100_001
visited[N] = 1

time = 0
cnt = 1
def bfs(queue):
    while queue:

        current = queue.popleft()

        for nx in (current - 1, current + 1, current * 2):
            if 0 <= nx < 100_001:
                visited[nx] = visited[current] + 1
                
                queue.append(nx)

time = bfs(queue)
if time == bfs(queue):
    cnt += 1


print(time)
print(cnt)