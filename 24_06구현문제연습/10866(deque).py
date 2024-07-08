from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())


dq = deque()
for _ in range(N):
    command = input().rstrip()
    
    if command.startswith("push_front"):
        _, num = command.split()
        dq.appendleft(int(num))
    elif command.startswith("push_back"):
        _, num = command.split()
        dq.append(int(num))
    elif command == "pop_front":
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif command == "pop_back":
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif command == "size":
        print(len(dq))
    elif command =="empty":
        if not dq:
            print(1)
        else:
            print(0)
    elif command == "front":
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif command == "back":
        if not dq:
            print(-1)
        else:
            print(dq[-1])