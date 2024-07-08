from collections import deque

N = int(input())
field = [[0] * (N+1) for _ in range(N+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    field[a][b] = 2#사과위치

snake = deque()
snake.append((1, 1))

command = []

for _ in range(int(input())):
    t, d = input().split()
    command.append((int(t), d))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#상, 우, 하, 좌

time = 0
direct = 1

def left(look):
    return (look+3) % 4

def right(look):
    return (look+1) % 4



while True:
    x, y = snake[0]#덱구조도 [0]가능
    head_x = x + dx[direct]
    head_y = y + dy[direct]
    if head_x <= 0 or head_x > N or head_y <= 0 or head_y > N or (head_x, head_y) in snake:
        break
    
    if field[head_x][head_y] == 2:
            field[head_x][head_y] = 0
            snake.appendleft((head_x, head_y))
    else:
        snake.appendleft((head_x, head_y))
        snake.pop()
    
    """
    a, b = snake.pop()
        field[a][b] = 0
    """
    time += 1
    
    if command and time == command[0][0]:#왼쪽 평가 이후 시간 비교
        command_t, command_d = command.pop(0)
        if command_d == 'L':
            direct = left(direct)
        else:
            direct = right(direct)

print(time+1)#시간 +1을해야 정답이네 뭐고..