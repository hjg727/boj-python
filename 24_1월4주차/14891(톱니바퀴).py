from collections import deque

gear = [deque(list(map(int, input()))) for _ in range(4)]

K = int(input())

command = deque()

for _ in range(K):
    target, direct = map(int, input().split())
    command.append((target - 1, direct))

def rotate(gear, direction):
    if direction == 1:
        right = gear.pop()
        gear.appendleft(right)
    elif direction == -1:
        left = gear.popleft()
        gear.append(left)
    return gear

for _ in range(K):
    position = []
    target, direct = command.popleft()
    
    if target == 1:
        if gear[target][2] != gear[target+1][6]:
            position.append((target+1, -direct))
            #gear[target+1] = rotate(gear[target+1], -direct)
            if gear[target+1][2] != gear[target+2][6]:
                position.append((target+2, direct))
                #gear[target+2] = rotate(gear[target+2], direct)

        if gear[target][6] != gear[target-1][2]:
            position.append((target-1, -direct))
            #gear[target-1] = rotate(gear[target-1], -direct)
        
    if target == 2:
        if gear[target][2] != gear[target+1][6]:
            position.append((target+1, -direct))
            #gear[target+1] = rotate(gear[target+1], -direct)

        if gear[target][6] != gear[target-1][2]:
            position.append((target-1, -direct))
            #gear[target-1] = rotate(gear[target-1], -direct)
            if gear[target-1][6] != gear[target-2][2]:
                position.append((target-2, direct))
                #gear[target-2] = rotate(gear[target-2], direct)
        
    if target == 0:
        if gear[target][2] != gear[target+1][6]:
            position.append((target+1, -direct))
            #gear[target+1] = rotate(gear[target+1], -direct)

            if gear[target+1][2] != gear[target+2][6]:
                position.append((target+2, direct))
                #gear[target+2] = rotate(gear[target+2], direct)
                if gear[target+2][2] != gear[target+3][6]:
                    position.append((target+3, -direct))
    if target == 3:
        if gear[target][6] != gear[target-1][2]:
            position.append((target-1, -direct))
            
            if gear[target-1][6] != gear[target-2][2]:
                position.append((target-2, direct))

                if gear[target-2][6] != gear[target-3][2]:
                    position.append((target-3, -direct))

    gear[target] = rotate(gear[target], direct)
    for t, d in position:
        gear[t] = rotate(gear[t], d)

point = 0
if gear[0][0] == 1:
    point += 1
if gear[1][0] == 1:
    point += 2
if gear[2][0] == 1:
    point += 4
if gear[3][0] == 1:
    point += 8

print(point)