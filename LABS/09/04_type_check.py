def type_check(ty):
    def decorator(func):
        def wrapper(*args,**kwargs):
            is_of_type = all(isinstance(obj,ty) for obj in args)
            if is_of_type:
                return func(*args, **kwargs)
            return 'Bad Type'

        return wrapper
    return decorator


@type_check(str)

def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))