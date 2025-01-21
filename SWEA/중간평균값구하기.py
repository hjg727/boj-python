T = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    hap = 0

    num.remove(max(num))
    num.remove(min(num))

    for x in num:
        hap += x
    res = round(hap/len(num))
    print(f"#{test_case} {res}")