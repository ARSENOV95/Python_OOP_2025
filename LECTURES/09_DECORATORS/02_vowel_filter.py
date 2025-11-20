from functools import wraps


def vowel_filter(function):
    vowels_list = ['a','e','i','o','u']
    @wraps(function)
    def wrapper():
        result = function()
        vowels = [i for i in result if i.lower() in vowels_list]
        return vowels
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())