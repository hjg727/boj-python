T = int(input())
for test_case in range(1, T+1):
    N, cnt = map(int, input().split())

    digits = list(str(N))
    n = len(digits)
    max_prize = 0
    visited = set()

    def dfs(digits, count):
        global max_prize

        current_state = ("".join(digits), count)#"".join(digits)혹은 tuple(digits)를 써야된다. 
        #왜? set()은 해시가능성이 있기때문에 리스트는 set안에 저장 불가능하다 그러나 tuple이나 문자열로 저장 가능
        if current_state in visited:
            return
        visited.add(current_state)

        if count == cnt:
            max_prize = max(max_prize, int("".join(digits)))
            return
        
        for i in range(n):
            for j in range(i+1, n):
                digits[i], digits[j] = digits[j], digits[i]
                dfs(digits, count + 1)
                digits[i], digits[j] = digits[j], digits[i]
    
    dfs(digits, 0)
    
    print(f"#{test_case} {max_prize}")
