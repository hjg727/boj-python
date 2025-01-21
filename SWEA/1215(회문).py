def valid(word):
    if word == word[::-1]:
        return True
    return False

def check(word_list, length):
    cnt = 0
    for start in range(8-length+1):
        if valid("".join(word_list[start:start+length])):
            cnt += 1
    return cnt

for test_case in range(1, 11):
    
    length = int(input())
    
    puzzle = [list(map(str, input().strip())) for _ in range(8)]
    res = 0
    for row in puzzle:
        res += check(row, length)
    
    for col in range(8):
        column = []
        for row in range(8):
            column.append(puzzle[row][col])
        res += check(column, length)
    
    print(f"#{test_case} {res}")