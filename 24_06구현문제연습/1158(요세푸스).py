from collections import deque

N, K = map(int, input().split())

circle = deque(range(1, N+1))

res = []
while circle:
    circle.rotate(-(K-1))

    if len(circle) == 1:
        res.append(str(circle.popleft()))
    else:
        res.append(str(circle.popleft()) + ",")

print("<"+" ".join(res)+">")