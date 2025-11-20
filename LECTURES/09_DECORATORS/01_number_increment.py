def number_increment(numbers : list):
    def increase():
        increased = [num + 1 for num in numbers]
        return increased

    return increase()


print(number_increment([1, 2, 3]))