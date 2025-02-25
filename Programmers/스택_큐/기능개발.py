progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]	
answer = [2, 1]

success = []

import math

def solution(progresses, speeds):

    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    success = []
    tmp_max = days[0]
    cnt = 1
    for i in range(1, len(days)):
        if days[i] > tmp_max:
            success.append(cnt)
            tmp_max = days[i]
            cnt = 1
        else:
            cnt += 1
    
    success.append(cnt)
    return success



def solution1(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
    
print(solution1(progresses, speeds))