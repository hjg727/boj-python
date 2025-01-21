T = int(input())

valid = set(range(10))

for test_case in range(1, T+1):
    N = int(input())
    sheep = N
    cnt = 1
    res = set()

    while res != valid:
        
        for i in str(sheep):
            if i not in res:
                res.add(int(i))
        
        if res == valid:
            break

        cnt += 1
        sheep = N * cnt
            
    print(f"#{test_case} {sheep}")