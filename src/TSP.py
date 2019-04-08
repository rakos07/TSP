import random, copy, numpy, math, matplotlib.pyplot as plt

points = [random.sample(range(100), 2) for x in range(11)];
travel = random.sample(range(11), 11);

for tlp in numpy.logspace(0, 5, num = 100000)[::-1]:
    [i, j] = sorted(random.sample(range(11), 2));
    newTravel = travel[:i] + travel[j:j + 1] + travel[i + 1:j] + travel[i:i + 1] + travel[j + 1:];
    if math.exp((sum([math.sqrt(sum([(points[travel[(k + 1) % 11]][d] - points[travel[k % 11]][d]) ** 2 for d in [0, 1]])) for k in [j, j - 1, i, i - 1]])
                - sum([math.sqrt(sum([(points[newTravel[(k + 1) % 11]][d] - points[newTravel[k % 11]][d]) ** 2 for d in [0, 1]])) for k in [j, j - 1, i, i - 1]])
                ) / tlp) > random.random():
        travel = copy.copy(newTravel);
plt.plot([points[travel[i % 11]][0] for i in range(12)], [points[travel[i % 11]][1] for i in range(12)], 'xb-');
plt.show()



