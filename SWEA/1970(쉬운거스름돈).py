T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    change = []

    change.append(N // 50000)
    change.append((N - 50000*change[0])//10000)
    change.append(N%10000 // 5000)
    change.append((N%10000 - (change[2]*5000)) // 1000)
    change.append(N%1000 // 500)
    change.append((N%1000 - (change[4]*500)) // 100)
    change.append(N%100 // 50)
    change.append((N%100 - (change[6]*50)) // 10)

    print(f"#{test_case}")
    print(" ".join(map(str, change)))