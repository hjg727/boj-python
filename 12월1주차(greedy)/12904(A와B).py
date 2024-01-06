S = input().strip()
T = input().strip()
#list로받지말고 문자열로받아야한다.
#문자열을 리스트로 받게되면, 리스트의 각 요소를 문자열로 다뤄야한다.


while len(S) != len(T):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]
        #T = T[:-1][::-1]
if T == S:
    print(1)
else:
    print(0)
'''
from collections import deque

S = input().strip()
T = input().strip()

queue = deque([S])

while queue:
    current = queue.popleft()
    if current == T:
        print(1)
        break
    if len(current) < len(T):
        queue.append(current + 'A')
        queue.append(current[::-1] + 'B')
else:
    print(0)
너비 우선 탐색(Breadth First Search, BFS)은 모든 가능한 경우의 수를 동일한 깊이에서 탐색하는 알고리즘입니다. 
이는 특정 조건을 만족하는 경우의 수를 찾을 때 매우 유용한 방법입니다. 
BFS는 특히 최소 횟수 또는 최단 경로를 찾는 문제에서 자주 사용됩니다.

이 문제에서 BFS를 사용하게 된 근거는 다음과 같습니다:

1. 문제의 요구사항: S에서 시작하여 T를 만드는 과정에서 'A'를 추가하거나, 문자열을 뒤집고 'B'를 추가하는 두 가지 연산을 사용할 수 있습니다. 
이는 가능한 모든 경우의 수를 탐색해야 하는 문제로, BFS를 사용하기 적합합니다.
2. 최소 횟수/최단 경로: BFS는 모든 가능한 경우의 수를 동일한 깊이에서 탐색하므로, 가장 먼저 조건을 만족하는 경우를 찾게 되면 그것이 최소 횟수 또는 최단 경로일 확률이 높습니다. 
이 문제에서는 S에서 T를 만드는 최소 횟수를 찾는 것이 아니지만, BFS를 통해 가장 먼저 T와 같아지는 문자열을 찾을 수 있습니다.
하지만 이 문제에서는 BFS로 인해 메모리 초과가 발생하는 문제가 있습니다. 
이는 T의 길이가 크다면 그에 따라 생성되는 경우의 수가 기하급수적으로 늘어나기 때문입니다. 
따라서, 이 문제를 해결하기 위한 더 효율적인 방법은 T에서 S로 가는 방향으로 문제를 접근하는 것입니다.
'''