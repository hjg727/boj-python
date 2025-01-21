T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    res = {2: 0,
           3: 0,
           5: 0,
           7: 0,
           11: 0}
    
    for i in res.keys():
        while N % i == 0:
            res[i] += 1
            N //= i
    print(f"#{test_case}", end=" ")
    print(" ".join(map(str, res.values())))