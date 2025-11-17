class countdown_iterator:
    def __init__(self,count :int):
        self.count = count
        self.current_count = self.count + 1

    def __iter__(self):
        return self


    def __next__(self):
        self.current_count -= 1
        if self.current_count >= 0:
            return self.current_count
        else:
            raise StopIteration

iterator = countdown_iterator(10)

for item in iterator:
    print(item, end=" ")
