import time

def exec_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time() #.time() function is a timestam stoest in a variable to log the start time
        func(*args,**kwargs)
        end_time = time.time()
        return end_time - start_time


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string

    return result


print(concatenate(["a" for i in range(1000000)]))