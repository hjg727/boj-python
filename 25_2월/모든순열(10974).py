import itertools
arr = [i for i in range(1, int(input())+1)]
perm_iterator = itertools.permutations(arr,2)
for perm in perm_iterator:
    print(*perm)