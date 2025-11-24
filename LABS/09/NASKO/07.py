class store_results:
    def __init__(self,file_name):
        self.file_name = file_name

    def __call__(self,func):
        def wrapper (*args, **kwargs):
            result = func(*args, **kwargs)
            with open(self.file_name,'a') as f:
                f.write(f"Function {func.__name__} was called. Result: {result}\n")
        return wrapper()


@store_results('results.txt')
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)