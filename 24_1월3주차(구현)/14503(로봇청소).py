import sys
input = sys.stdin.readline
#벽 = 1, 더러움 = 0, 치움 = 2

N, M = map(int, input().split())
robot_x, robot_y, direct = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#북 동 남 서

dirty = True

field[robot_x][robot_y] = 2
count = 1

def left(look):#왼쪽으로 방향전환 함수
    return (look + 3) % 4
#return (look-1) % 4

while dirty:
    clean = False
    for _ in range(4):#드러운 곳 탐색
        direct = left(direct)
        move_x = robot_x + dx[direct]
        move_y = robot_y + dy[direct]
        if field[move_x][move_y] == 0:
            field[move_x][move_y] = 2
            count += 1
            robot_x, robot_y = move_x, move_y
            clean = True
            break
    
    if not clean:#만약 4칸 중 청소되지 않은 빈 칸이 없는 경우

        if field[robot_x - dx[direct]][robot_y - dy[direct]] == 1:
            break# while문 탈출 동작 그만

        else:
            robot_x, robot_y = robot_x - dx[direct], robot_y - dy[direct]

print(count)
#DFS, BFS