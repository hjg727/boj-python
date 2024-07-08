#쇠파이프
import sys
input = sys.stdin.readline
pipes = list(input().rstrip())

cnt = 0
prev = ""
res = 0

for pipe in pipes:

    if pipe == "(":    
        
        cnt += 1
        prev = "("

    elif pipe == ")":

        if prev == "(":
            cnt -= 1
            res += cnt
        elif prev == ")":
            res += 1
            cnt -= 1
        prev = ")"
print(res)