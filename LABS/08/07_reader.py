def read_next(*args):
    for el in args:
         for i in el:
             yield i


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)