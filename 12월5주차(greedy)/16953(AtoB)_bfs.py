from collections import deque

A, B = map(int, input().split())
queue = deque([(A, 1)])

while queue:
    value, count = queue.popleft()
    if value == B:
        print(count)
        break
    if value * 2 <= B:
        queue.append((value*2, count+1))
    if int(str(value) + '1') <= B:
        queue.append((int(str(value)+'1'), count+1))
else:
    print(-1)
