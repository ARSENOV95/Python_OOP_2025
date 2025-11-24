class sequence_repeat:
    def __init__(self,sequence: str,number :int):
        self.sequence = sequence
        self.number = number #the number will represent the last index
        self.curr_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index < self.number:
            i = self.curr_index
            self.curr_index += 1

            if i >= len(self.sequence):
                i = i - len(self.sequence)
            return self.sequence[i]
        raise  StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')