for test_case in range(1, 11):
    N = int(input())
    build = list(map(int, input().split()))

    res = 0

    for i in range(2, len(build)-2):
        compare = max(build[i-2], build[i-1], build[i+1], build[i+2])
        if build[i] > compare:
            res += build[i] - compare
    
    print(f"#{test_case} {res}")

# a = [0, 0, 1, 2, 3, 0, 0]
# for i in range(2, 7-2):
#     print(a[i], end=" ") 1 2 3