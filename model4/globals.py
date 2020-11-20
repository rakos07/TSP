import random
import math

xMax = 100
yMax = 100
seedValue = 1
numNodes = 40
numGenerations = 20
populationSize = 20
mutationRate = 0.02
tournamentSize = 1
elitism = True
numDeliverer = 2

def random_range(n, total):
    dividers = sorted(random.sample(range(1, total), n - 1))

    print([a - b for a, b in zip(dividers + [total], [0] + dividers)])

    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def route_lengths():
    upper = (numNodes + numDeliverer - 1)
    fa = upper / numDeliverer * 1.6
    fb = upper / numDeliverer * 0.6
    a = random_range(numDeliverer, upper)
    while 1:
        if all( i < fa and i > fb  for i in a):
                break
        else:
                a = random_range(numDeliverer, upper)
    return a
