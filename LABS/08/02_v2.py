class dictionary_iter:
    def __init__(self,obj :dict):
        self.obj = obj
        self.pairs = tuple((key,val) for key,val in obj.items()) #we can create a tuple with tupels in the codintion to avoid complciation si in the next clause
        self.curr_pair = -1

    def __iter__(self):
        return self

    def __next__(self):
        for pair in
        self.curr_pair += 1
        if self.curr_pair  < len(self.obj):
            return self.pairs[self.curr_pair]
        else:
            raise StopIteration



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)