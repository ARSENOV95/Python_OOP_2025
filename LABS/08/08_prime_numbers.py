def get_primes(ints :list):
    for num in ints:
        if num == 0 or num == 1 or num < 0:
            continue

        if num % num == 0:
            if num //1 == num:
                yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))