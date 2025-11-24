from math import sqrt

def get_primes(numbers :list):
    for number in numbers:
        if number < 2:
            continue

        for i in range(2,int(sqrt(number)) + 1): # +1 is incase int floors the number
            if number % i == 0:  #if the current number devies modulo to any number from 2 to the number - 1 its not a prime
                break


        else:
            yield number
