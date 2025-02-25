from collections import deque

L = int(input())

for _ in range(L):
    password = list(input().strip())
    left = deque()
    right = deque()

    for word in password:
        if word == "<":
            if left:
                right.appendleft(left.pop())
        elif word == ">":
            if right:
                left.append(right.popleft())
        elif word == "-":
            if left:
                left.pop()
        else:
            left.append(word) 
    
    print("".join(left)+"".join(right))