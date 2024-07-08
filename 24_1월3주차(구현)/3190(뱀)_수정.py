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
    t = int(t)
    command.append((t, d))

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
    if field[head_x][head_y] == 1 or (head_x, head_y) in snake:
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
    
    if time == command[0][0] and command:
        command_t, command_d = command.pop(0)
        if command_d == 'L':
            direct = left(direct)
        else:
            direct = right(direct)

print(time)

"""
위의 코드는 기존 코드의 구조를 최대한 유지하면서 수정한 것이므로, 더 효율적인 구현 방법이 있을 수 있습니다. 
예를 들어, 뱀의 몸통을 나타내는 snake를 리스트 대신 집합으로 관리하면 뱀이 자신의 몸과 부딪히는 경우를 더 빠르게 판단할 수 있습니다.
"""