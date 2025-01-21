"""
N*N 보드에 N개의 퀸을 서로 다른 두 퀸을 공격하지 못하게 놓는 경우의 수는 몇가지?
"""
T = int(input())

def valid(row, col, cols, n_pos, p_pos):
    if col in cols or (row-col) in n_pos or (row+col) in p_pos:
        return False
    return True


for test_case in range(1, T+1):
    N = int(input())

    cols = set()
    p_pos = set()
    n_pos = set()
    cnt = 0

    def dfs(row, cols, n_pos, p_pos, N):
        global cnt

        if row == N:
            cnt += 1
            return
        
        for col in range(N):
            if valid(row, col, cols, n_pos, p_pos):
                cols.add(col)
                n_pos.add(row-col)
                p_pos.add(row+col)

                dfs(row+1, cols, n_pos, p_pos, N)

                cols.remove(col)
                n_pos.remove(row-col)
                p_pos.remove(row+col)
    
    dfs(0, cols, n_pos, p_pos, N)

    print(f"#{test_case} {cnt}")