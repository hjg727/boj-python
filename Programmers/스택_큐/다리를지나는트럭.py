"""
bridge_length => 다리에 올라갈 수 있는 트럭 수 이자 다리 길이
weight => 다리가 견딜 수 있는 무게
truck_weights=> 트럭별 무게
최소 시간을 여기서 보장하는건 최대한 많이 다리에 겹겹이 태우고 지나가게 하는 것
다리에 초기설정(첫 차 올라가기)

time = 한번에 차 올라간 숫자 + 다리길이
결과는 time의 누적합
"""
from collections import deque
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = [truck_weights.popleft()]
    res = 0
    time = 1

    while truck_weights:
        if len(bridge) + 1 <= bridge_length and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
            time += 1
        else:
            res += time + bridge_length
            if truck_weights:
                bridge = [truck_weights.popleft()]
                time = 0
    if bridge:
        res += time + bridge_length
    return res
print(solution(bridge_length, weight, truck_weights))

from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    current_weight = 0
    while len(truck_weights) > 0:
        time += 1
        current_weight -= bridge.popleft()
        if current_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
    return time + bridge_length

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length)  # [0]*bridge_length 을 덱으로 변환
    truck_weights = deque(truck_weights) # 리스트를 덱으로 변환
    
    currentWeight = 0
    while len(truck_weights) > 0:
        time = time + 1

        currentWeight = currentWeight - bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight = currentWeight + truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    time = time + bridge_length
    
    return time