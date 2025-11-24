class vowels:
    vowels_list = ['a','e','i','o','u','y']

    def __init__(self,text):
        self.text = text
        self.vowels = [el for el in self.text if el.lower() in self.vowels_list]
        self.current = -1

    def __iter__(self):
        return  self

    def __next__(self):
        self.current += 1
        if self.current >= len(self.text):
            raise StopIteration

        else:
            return self.vowels[self.current]


