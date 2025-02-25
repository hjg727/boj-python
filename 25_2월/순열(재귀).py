def permutation(arr):
    if len(arr) <= 1:
        return [arr]
    
    result = []

    for i in range(len(arr)):
        current = arr[i]

        remaining = arr[:i] + arr[i+1:]

        for p in permutation(remaining):
            result.append([current] + p)
    
    return result
N = int(input())
A = [i for i in range(1, N+1)]
permutations = permutation(A)

for perm in permutations:
    print(*perm)