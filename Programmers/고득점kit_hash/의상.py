"""
def solution(clothes):
    map = {}
    answer = 0
    for cloth in clothes:
        map.setdefault(cloth[1], []).append(cloth[0])
        answer += 1
    
    #여기서 서로 조합을 하며 풀어나가야되는데.. 몇개를 조합할지를 모르니까 종류의 갯수끼리 곱하기
    if len(map) > 1:
        cnt = 1
        for cloth in map:
            cnt *= len(map[cloth])
        answer += cnt
        return answer
    else:
        return answer
"""

def solution(clothes):
    map = {}
    answer = 0
    for cloth in clothes:
        map.setdefault(cloth[1], []).append(cloth[0])
    
    #여기서 서로 조합을 하며 풀어나가야되는데.. 몇개를 조합할지를 모르니까 종류의 갯수끼리 곱하기
    cnt = 1
    for cloth in map:
        cnt *= len(map[cloth])+1
    answer += cnt
    return answer-1
