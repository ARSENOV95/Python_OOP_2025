def  multiply(multiplier):  #ако имаме параметър който трябва да участва в декореатора е необходимо да направим още една референция към рапнатата функция
    def decorator(funct): #ниво 2 прави референция към фунцикята - това е нивото в което декроатора прави връзката към референицятана функцията
        def wrapper(*args,**kwargs): #niwo 3 рапва функцията иразширрява логиата - взима резултата от изплънението на функцията и го умножава по параметъра
            result = funct(*args,**kwargs)
            return  result * multiplier

        return wrapper
    return decorator



@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))