def even_parameters(func):
    def wrapper(*args, **kwargs):

        nums = all(isinstance(num, int) for num in
                   args)  # check if all args are numeric (tried with is digint and did not work for tuiple)

        if nums:
            if all(num % 2 == 0 for num in
                   args):  # check if all numebrs are even, and if Y, retrun the result fo the fucntion
                result = func(*args, **kwargs)
                return result

        return 'Please use only even numbers!'

    return wrapper
