T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = []
    for _ in range(N):
        char, count = input().split()
        count = int(count)
        data.append((char, count))
    
    res = "".join(char*count for char, count in data)

    print(f"#{test_case}")

    for i in range(0, len(res), 10):
        print(res[i:i+10])