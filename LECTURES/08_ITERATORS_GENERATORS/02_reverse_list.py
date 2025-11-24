class reverse_iter:
    def __init__(self, lst :list):
        self.lst = lst[::-1]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.lst):
            return self.lst[self.index]
        else:
            raise StopIteration

reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)