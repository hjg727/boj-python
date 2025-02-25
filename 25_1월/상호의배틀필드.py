"""

문자	의미
.	평지(전차가 들어갈 수 있다.) 0
*	벽돌로 만들어진 벽 1
#	강철로 만들어진 벽 2
-	물(전차는 들어갈 수 없다.) -1
^	위쪽을 바라보는 전차(아래는 평지이다.) a
v	아래쪽을 바라보는 전차(아래는 평지이다.) b 
<	왼쪽을 바라보는 전차(아래는 평지이다.) c
>	오른쪽을 바라보는 전차(아래는 평지이다.) d

사용자가 넣을 수 있는 입력의 종류
U up: 전차가 바라보는 방향을 위쪽으로 변경, "한칸위의 칸이 평지라면" 그 칸으로 이동
D down: 아래쪽으로 변경, "한칸아래의 칸이 평지라면" 그칸으로이동
L
R
S shoot: 전차가 현재 바라보는 방향으로 포탄을 발사

포탑을 발사할 때, 
포탄은 "벽돌 벽 혹은 강철 벽에 충돌"하거나 "게임 맵 밖으로 나갈 때"까지 직진.
벽에맞으면 포탄은 소멸, 벽돌벽이면 그 벽은 평지로 전환
강철벽이면 포탄만 소멸

사용자 모든 입력을 처리하면 게임 맵의 상태가 어떤지 보여주기

direct = {
    "U" : (1,0),
    "D" : (-1,0),
    "R" : (0,1),
    "L" : (-1,0)   
}

char_to_value = {
    '.': 0, #평지
    '_': -1, #물
    '*': 1, #벽돌
    '#': 2, #강철
    '<': 'l', #좌
    '>': 'r', #우
    'v': 'd', #하
    '^': 'u' #상
}
T = int(input())

for test in range(1, T+1):
    H, W = map(int, input().split())
    input_data = []

    for _ in range(H):
        row = input().rstrip()
        input_data.append(row)

    N = int(input())
    field = [[char_to_value[char] for char in row] for row in input_data]
    command = list(str(input().rstrip()))
"""

direct = {
        '^': (-1, 0),
        'v': (1, 0),   
        '<': (0, -1),  
        '>': (0, 1)    
    }
T = int(input())

for test_case in range(1, T+1):
    H, W = map(int, input().split())
    
    field = []
    for _ in range(H):
        row = list(input().rstrip())
        field.append(row)
    
    tank = 0
    for i in range(H):
        for j in range(W):
            if field[i][j] in direct:
                tank = (i, j, field[i][j])
                break
        if tank:
            break
        
    N = int(input())
    commands = list(str(input().rstrip()))
    
    x, y, current_dir = tank

    for command in commands:

        if command == 'U':
            current_dir = '^'
            nx, ny = x + direct['^'][0], y + direct['^'][1]
            if 0<=nx<H and 0<=ny<W and field[nx][ny] == '.':
                field[x][y] = '.'
                x,y = nx, ny
        elif command == 'D':
            current_dir = 'v'
            nx, ny = x + direct['v'][0], y + direct['v'][1]
            if 0<=nx<H and 0<=ny<W and field[nx][ny] == '.':
                field[x][y] = '.'
                x,y = nx, ny
        elif command == 'R':
            current_dir = '>'
            nx, ny = x + direct['>'][0], y + direct['>'][1]
            if 0<=nx<H and 0<=ny<W and field[nx][ny] == '.':
                field[x][y] = '.'
                x,y = nx, ny
        elif command == 'L':
            current_dir = '<'
            nx, ny = x + direct['<'][0], y + direct['<'][1]
            if 0<=nx<H and 0<=ny<W and field[nx][ny] == '.':
                field[x][y] = '.'
                x,y = nx, ny
        elif command == 'S':
            dx,dy = direct[current_dir]
            nx, ny = x + dx, y + dy
            while 0<=nx<H and 0<=ny<W:
                if field[nx][ny] == '*':
                    field[nx][ny] = '.'
                    break
                elif field[nx][ny] == '#':
                    break
                nx, ny = nx+dx, ny+dy
    
    field[x][y] = current_dir
    print(f"#{test_case}", end =" ")

    for i in range(H):
        print("".join(map(str, field[i])))


"""
사용자가 넣을 수 있는 입력의 종류
U up: 전차가 바라보는 방향을 위쪽으로 변경, "한칸위의 칸이 평지라면" 그 칸으로 이동
D down: 아래쪽으로 변경, "한칸아래의 칸이 평지라면" 그칸으로이동
L
R
S shoot: 전차가 현재 바라보는 방향으로 포탄을 발사
포탑을 발사할 때, 
포탄은 "벽돌 벽 혹은 강철 벽에 충돌"하거나 "게임 맵 밖으로 나갈 때"까지 직진.
벽에맞으면 포탄은 소멸, 벽돌벽이면 그 벽은 평지로 전환
강철벽이면 포탄만 소멸
"""