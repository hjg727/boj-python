N, M = map(int, input().split())

def dfs(start, sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    # start부터 N까지 반복하여, 현재 선택한 수 이상의 값만 선택하도록 함.
    for i in range(start, N+1):
        sequence.append(i)
        dfs(i, sequence)  # 재귀 호출 시 현재 i부터 선택 (비내림차순 보장)
        sequence.pop()     # 백트래킹

dfs(1, [])