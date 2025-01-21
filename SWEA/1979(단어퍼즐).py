T = int(input())

def check(puzzle, K):
    cnt, tmp = 0, 0
    for i in puzzle:
        if i == 1:
            tmp += 1
        else:
            if tmp == K:
                cnt += 1
                tmp = 0
            else:
                tmp = 0
    if tmp == K:
        cnt += 1
    return cnt

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    res = 0

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    for row in puzzle:
        res += check(row, K)
    
    for col in range(len(puzzle[0])):
        col_list = [puzzle[row][col] for row in range(len(puzzle))]
        res += check(col_list, K)
    
    print(f"#{test_case} {res}")