#행 검증
#열 검증
def is_valid(array):
    valid_set = set(range(1, 10))
    for row in array:
        if set(row) != valid_set:
            return False
    
    for col in range(9):
        column = [array[row][col] for row in range(9)]
        if set(column) != valid_set:
            return False
    #3*3 검증
    for start_x in range(0, 9, 3):
        for start_y in range(0, 9, 3):
            block = set()

            for i in range(3):
                for j in range(3):
                    num = array[start_x+i][start_y+j]
                    block.add(num)
            
            if block != valid_set:
                return False
            
    return True

T = int(input())
for test_case in range(1, T+1):
    sdoque = [list(map(int, input().split())) for _ in range(9)]

    if is_valid(sdoque):
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")