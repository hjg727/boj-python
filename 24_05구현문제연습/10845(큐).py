from collections import deque
import sys
input = sys.stdin.readline
q = deque([])

N = int(input().strip())

for _ in range(N):
    command = input().strip()

    if command.startswith("push"):
        _, num = command.split()
        q.appendleft(int(num))
    elif command == "pop":
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif command == "front":
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif command == "back":
        if not q:
            print(-1)
        else:
            print(q[0])
