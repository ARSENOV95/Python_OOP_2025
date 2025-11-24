class take_skip:
    def __init__(self,step :int,count :int):
        self.step = step
        self.count = count
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1 # -1  + 1 =0 as per condtion - count will be the len so its just like and index form 0 -5
        if self.current < self.count:
            return self.current * self.step
        else:
            raise StopIteration

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
