def fibonacci():
    current_num,next_num = 0,1

    while True:
        yield current_num
        current_num  = next_num
        next_num = current_num + next_num