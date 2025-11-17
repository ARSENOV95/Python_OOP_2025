def possible_permutations(seq :list):
    last_seq = seq

    while True:
        new_seq = set(seq)
        if new_seq != last_seq:
            yield last_seq
            last_seq = new_seq
        if new_seq == seq:
            break




[print(n) for n in possible_permutations([1, 2, 3])]

