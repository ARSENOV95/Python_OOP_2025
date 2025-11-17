class dictionary_iter:
    def __init__(self,dictionary: dict):
        self.dictionary = tuple(dictionary.items()) #returns a tuple with tuples .items returns an interable with key:val tuples
        self.i = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.dictionary):
            i = self.i
            self.i += 1
            return self.dictionary[i]
        raise StopIteration()