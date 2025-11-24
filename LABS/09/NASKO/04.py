def type_check(param_type):
    def decorator(func):
        def wrapper(param):
            if isinstance(param,param_type):
                return func(param)
            return 'Bad type'
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))