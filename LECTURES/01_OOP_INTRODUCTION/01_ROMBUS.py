def top(num):
    result = ''
    for row in range(1,num + 1):
        result += f"{(' ' * (num - row)) + '* ' * row}\n"
    return result

def bottom(num):
    result = ''
    for row in range(1,num):
        result += f"{(' ' * (row)) + '* ' * (num - row)}\n"
    return result

def rombus(num):
    result = top(num) + bottom(num)

    return result

n = int(input())

print(rombus(n))

