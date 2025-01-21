T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    
    item_list = list(map(int, input().split()))
    max_num = item_list[-1]
    
    res = 0
    
    for i in range(N-2, -1, -1):
        if item_list[i] >= max_num:
            max_num = item_list[i]
        else:
            res += max_num - item_list[i]
    
    print(f"#{test_case} {res}")