def fibonacci(): #example  1st iter
    c = 0 #0
    n = 1 #1
    while True:
        yield c #1
        c,n = n,c + n #next number will be the sum of  c + n , c= n = 1 from the sequence, n  = c + n # the next number will be the sum of current + next in our case 0 + 1

generator = fibonacci()
for i in range(5): #nuber of iteration - 4
    print(next(generator))

