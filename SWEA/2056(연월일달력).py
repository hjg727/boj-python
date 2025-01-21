T = int(input())

for test_case in range(1, T+1):
    ymd = str(input())
    y = ymd[:4]
    m = ymd[4:6]
    d = ymd[6:]

    if int(m) == 2:
        if 1<=int(d)<=28:
            print(f"#{test_case} {y}/{m}/{d}")
        else:
            print(f"#{test_case} -1")
    elif int(m) in (1, 3, 5, 7, 8, 10, 12):
        if 1<=int(d)<=31:
            print(f"#{test_case} {y}/{m}/{d}")
        else:
            print(f"#{test_case} -1")
    elif int(m) in (4, 6, 9, 11):
        if 1<=int(d)<=30:
            print(f"#{test_case} {y}/{m}/{d}")
        else:
            print(f"#{test_case} -1")
    else:
        print(f"#{test_case} -1")