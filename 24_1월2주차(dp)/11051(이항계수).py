import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
res = math.comb(N, M)
print(res%10007)