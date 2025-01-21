import heapq
import sys
N = int(input())
cards =[]

for i in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

res = 0

while len(cards) > 1:
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    hap = x + y

    #res에 합을 누적하고, 합결과를 다시 큐에 넣는다.
    res += hap
    heapq.heappush(cards, hap)
    #hap = 0

print(res)