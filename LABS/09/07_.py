class store_results:
    _output_file = 'results.txt'

    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        text = f"Function '{self.func.__name__}' was called. Result: {result}"

        with open(self._output_file,"a") as f:
            f.write(f'{text}\n')

@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)