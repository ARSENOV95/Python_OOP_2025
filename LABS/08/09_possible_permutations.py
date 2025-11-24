from itertools import permutations

def possible_permutations(seq :list):
    for perm in permutations(seq):
        yield list(perm)



[print(n) for n in possible_permutations([1, 2, 3])]

