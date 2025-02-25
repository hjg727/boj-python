def next_permutation(arr):
    # 1. 뒤에서부터 감소하지 않는 지점 찾기
    i = len(arr) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i <= 0:  # 마지막 순열이면 종료
        return None
    
    # 2. arr[i-1]보다 큰 값 찾기
    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1
    
    # 3. 교환
    arr[i-1], arr[j] = arr[j], arr[i-1]
    
    # 4. i부터 끝까지 뒤집기
    left, right = i, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

# 테스트
arr = [1, 2, 3, 4]
result = next_permutation(arr)
print(result)  # [1, 3, 2, 4]