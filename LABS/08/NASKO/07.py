def read_next(*args):
    for arg in args:
        yield from arg #reterns all elements from the sequence its a built in loop in yield for sequences
