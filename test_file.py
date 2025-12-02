from itertools import count

flowers = ['rose','tulip','rose','lotus']

counts = sum(1 for flower in flowers if flower == 'rose')

print(counts)