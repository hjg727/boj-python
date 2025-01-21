"""
1. 해당 위치의 사탕과 행, 열에 인접한 위치의 사탕의 색이 다르다면 교환
2. 교환된 상태에서 전체 맵에서 가장 긴 연속 부분 탐색(변경된 행과 열에 대해서만 탐색하고싶긴하다.)
3. 다시 제자리로 바꾸고 해당위치는 방문처리
"""
def find_max_cnt(line):
    max_cnt = 1
    current = 1
    previous = line[0]

    for candy in line[1:]:
        if candy == previous:
            current += 1
            max_cnt = max(max_cnt, current)
        else:
            previous = candy
            current = 1
    
    return max_cnt

def change_candy(board, x1, y1, x2, y2):
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]

    max_candy = 0
    board_row = set([x1,x2])
    for row in board_row:
        max_candy = max(max_candy, find_max_cnt(board[row]))
    
    board_col = set([y1,y2])
    for col in board_col:
        lines = [board[row][col] for row in range(N)]
        max_candy = max(max_candy, find_max_cnt(lines))
    
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]
    return max_candy

def check_change(board, x, y):
    max_candy = -1e9
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny <N and not visited[nx][ny]:
            max_candy = max(max_candy,change_candy(board, x, y, nx, ny))
    
    return max_candy

N = int(input())

board = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = []


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            res.append((check_change(board, i, j)))

print(max(res))