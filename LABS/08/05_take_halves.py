def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        ints = []
        for i in range(n):
            ints.append(seq[i])

        yield ints


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
