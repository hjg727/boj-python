T = int(input())

for test_case in range(1, T+1):

    cnt = 0

    goal = list(str(input().strip()))
    compare  = ['0']*len(goal)

    for i in range(len(goal)):
        if goal[i] != compare[i]:
            cnt += 1

            tmp = goal[i]

            for i in range(i+1, len(compare)):
                compare[i] = tmp
    
    print(f"#{test_case} {cnt}")