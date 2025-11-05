from functools import reduce

class Calculator:

    @staticmethod
    def add(*args):
        return  sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x,y: x*y,args)  #takes 2 elements using a lambda performs an action and removes the both and replaces them with results

    @staticmethod
    def divide(*args):
        try:
            return reduce(lambda x,y: x/y,args)
        except ZeroDivisionError:
            return "Cannot divide to 0"

    @staticmethod
    def subtract(*args):
        return reduce(lambda x,y: x-y,args)
