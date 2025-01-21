T = int(input())

calendar = {1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31}

for test_case in range(1, T+1):
    start_m, start_d, end_m, end_d = map(int, input().split())
    
    if start_m == end_m:
        print(f"#{test_case} {end_d - start_d + 1}")
        continue

    res = 0
    res = calendar[start_m] - start_d + 1
    start_m += 1

    if start_m == end_m:
        res = res + (end_d - 1 + 1)
        print(f"#{test_case} {res}")
        continue
    else:
        while start_m != end_m:
            res += calendar[start_m]
            start_m += 1
    
    res += (end_d - 1 + 1)

    print(f"#{test_case} {res}")