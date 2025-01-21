# N = int(input())

# cols = set() 
# n_pos = set()
# p_pos = set()
# cnt = 0

# def valid(row, col, cols, p_pos, n_pos):
#     if col in cols or (row + col) in p_pos or (row - col) in n_pos:
#         return False
#     return True

# def dfs(row, cols, p_pos, n_pos):
#     global cnt

#     if row == N:
#         cnt += 1
#         return
    
#     for col in range(N):
#         if valid(row, col, cols, p_pos, n_pos):
#             cols.add(col)
#             p_pos.add(row+col)
#             n_pos.add(row-col)
#             dfs(row+1, cols, p_pos, n_pos)
#             cols.remove(col)
#             p_pos.remove(row+col)
#             n_pos.remove(row-col)
# dfs(0,cols,p_pos,n_pos)

# print(cnt)

N = int(input())
cnt = 0

cols = [False] * N
p_pos = [False] * (2*N-1)
n_pos = [False] * (2*N-1)


def dfs(row):
    global cnt
    if row == N:
        cnt += 1
        return
    
    for col in range(N):
        if not cols[col] and not p_pos[row+col] and not n_pos[row-col+(N-1)]:
            cols[col] = True
            p_pos[row+col] = True
            n_pos[row-col+(N-1)] = True

            dfs(row+1)

            cols[col] = False
            p_pos[row+col] = False
            n_pos[row-col + (N-1)] = False

dfs(0)
print(cnt)