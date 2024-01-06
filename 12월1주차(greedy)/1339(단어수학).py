#두 문자열 중 긴 문자열에서 제일 앞에 있는 순대로 9
import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
#GCF, ACDEB

alpha = [0] * 26

for word in words:
    i = 0
    while word:
        cur = word[-1]
        word = word[:-1]
        alpha[ord(cur) - ord('A')] += (10**i)#매우 중요한 부분 복습때 다시 보기
        i += 1

alpha.sort(reverse=True)

ans = 0
t = 9

for i in range(26):
    if alpha[i] == 0:
        break
    ans += (t*alpha[i])
    t -= 1

print(ans)