from collections import deque

N = int(input())
field = [[0] * (N+1) for _ in range(N+1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    field[a][b] = 2#사과위치
for i in range(N+1):
    field[i][0] = field[i][N] = 1
    field[0][i] = field[N][i] = 1

snake = deque()
snake.append((1, 1))

command = []

for _ in range(int(input())):
    t, d = input().split()
    command.append((t, d))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#상, 우, 하, 좌

time = 0
direct = 1
length = 1

temp = deque()

def left(look):
    return (look+3) % 4
def right(look):
    return (look+1) % 4



while True:
    x, y = snake.pop()
    head_x = x + dx[direct]
    head_y = y + dy[direct]
    if field[head_x][head_y] == 1 and  (head_x, head_y) in snake:
        break
    elif field[head_x][head_y] == 2:#사과가 있을때
            length += 1
            snake.append((head_x, head_y))
            field[head_x][head_y] = 0
    else:
        while snake:
            nx, ny = snake.pop()
            move_nx = nx + dx[direct]
            move_ny = ny + dy[direct]
            field[move_nx][move_ny] = 1
            field[nx][ny] = 0
            temp.append((move_nx, move_ny))
    
    if temp:
        snake = temp

    
    time += 1
    
    if time == command[0][0]:
        command_t, command_d = command.pop(0)

        if command_d == 'L':
            direct = left(direct)
        else:
            direct = right(direct)

print(time)