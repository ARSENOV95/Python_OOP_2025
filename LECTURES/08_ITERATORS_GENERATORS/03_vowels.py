class vowels:
    def __init__(self,text :str):
        self.text = text
        self.vowels:
        self.index = -1

    def __vowels_check__(self):
        vowel = ['a', 'e', 'i', 'o', 'u']
        for char in self.text:
            if char in vowel:
                self.vowels.append(char)
        return self.vowels


    def __iter__(self):
        return self

    def __next__(self):
        self.__vowels_check__()
        self.index += 1
        if self.index < len(self.vowels):
            return self.vowels[self.indx]

        else:
            raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)