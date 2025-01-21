def solution(s):
    len_s = len(s)
    answer = 10000000
    for n in range(1, len_s//2 + 2):
        res = ""
        tmp = s[:n]
        cnt = 1
        
        for i in range(n, len(s)+n, n):
            if tmp == s[i:i+n]:
                cnt+=1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt)+tmp
                tmp = s[i:i+n]
                cnt = 1
        
        answer = min(answer,len(res))
            
    
    return answer