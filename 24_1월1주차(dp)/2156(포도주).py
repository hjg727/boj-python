N = int(input())

grape = [0]
for i in range(N):
    grape.append(int(input()))
dp = [0] * (N+1)
dp[1] = grape[1]#첫잔 이 그 값
if N > 1:
    dp[2] = grape[1] + grape[2]
for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + grape[i], dp[i - 3] + grape[i - 1] + grape[i])
print(dp[N])
'''
처음 문제를 접할때 dp[2] = grape[1] + grape[2]를 했을때는
그냥 grape에 값들어온 순서대로 바로 잔을 선택한다고생각했다.
그러나 더 dp스러운 생각방식은 첫번째 잔과 두번째 잔을 마셨다고생각하면 문제 이해가 보다 쉽다.
먼저, 각 포도주 잔을 마시는 경우의 수를 고려합니다. 이 때, 각 잔을 마시는 경우의 수는 다음의 세 가지 경우를 고려해야 합니다:
마지막 잔이 i번째 잔이라고 가정하면,
이전 잔을 마시지 않고 현재 잔을 마시는 경우 dp[i-2] + grape[i]
이전 잔을 마시고 현재 잔을 마시는 경우 dp[i-3] + grape[i-1] + grape[i]
현재 잔을 마시지 않는 경우 dp[i-1]
즉, 
i번째 잔을 마시지 않을 수도 있고(i-1번째 잔까지의 마실 수 있는 최대 양을 유지), 
i번째 잔만 마실 수도 있으며(i-2번째 잔까지의 최대 양에 i번째 잔의 양을 더함), 
또는 i-1번째 잔과 i번째 잔을 연속해서 마실 수도 있습니다(i-3번째 잔까지의 최대 양에 i-1번째 잔의 양과 i번째 잔의 양을 더함)
dp[N]은 N개의 잔이 있는데 최대한 마실수 있는 양이다.
'''