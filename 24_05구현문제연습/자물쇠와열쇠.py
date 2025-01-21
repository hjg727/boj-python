#회전 함수
def rotate_right(matrix):
    return [list(row) for row in zip(*matrix[::-1])]



def solution(key, lock):
    M = len(key)
    N = len(lock)
    count = 0
    extended_lock = [[0] * (N + M*2) for _ in range(N + M*2)]

    #중앙에 자물쇠 배치
    for i in range(N):
        for j in range(N):
            extended_lock[i+M][j+M] = lock[i][j]
    
    for rotate in range(4):
        
        key = rotate_right(key)
        
        #회전한 열쇠로 탐색 
        for x in range(1, N+M):#1~N+M-1까지인이유는 그림으로 그리면서 이해함
            for y in range(1, N+M):
                if match_lock(extended_lock, key, x, y, M, N): # 확장된 자물쇠, 열쇠2차원배열, x,y->시작좌표, M,N->배열의범위
                    return True
                    
                
    return False

#매칭결과
def match_lock(extended_lock, key, start_x, start_y, M, N):

    #확장된 자물쇠에 키배열값넣기 (만약 키의 돌기와 자물쇠의 홈이 안만나면 값이 1이 안나온다.)
    for i in range(M):#키의 범위까지
        for j in range(M):
            extended_lock[start_x+i][start_y+j] += key[i][j]
    
    for i in range(N):
        for j in range(N):
            if extended_lock[i+M][j+M] != 1:
                
                for i in range(M):
                    for j in range(M):
                        extended_lock[start_x+i][start_y+j] -= key[i][j]
                    
                return False
    
    return True

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))