import random, numpy, math, copy, matplotlib.pyplot as plt
pointCount = 10
restaurantCount = 4
restaurants = [random.sample(range(100), 2) for x in range(restaurantCount)];
for l in range(len(restaurants)):
    points = [random.sample(range(100), 2) for x in range(pointCount - 1)];
    points.insert(0, restaurants[l])
    travel = random.sample(range(pointCount),pointCount);
    for tlp in numpy.logspace(0,5,num=100000)[::-1]:
        [i,j] = sorted(random.sample(range(pointCount),2));
        newTravel = travel[:i] + travel[j:j+1] + travel[i+1:j] + travel[i:i+1] + travel[j+1:];
        newTravel.insert(0, newTravel.pop(newTravel.index(0)))

        point1 = sum([
            math.sqrt(
                sum([(
                        ((points[travel[(k+1) % pointCount]][d]) - (points[travel[k % pointCount]][d]))**2
                ) for d in [0, 1]])
            ) for k in [j, j-1, i, i-1]
        ])
        point2 = sum([math.sqrt(sum([(points[newTravel[(k+1) % pointCount]][d] - points[newTravel[k % pointCount]][d])**2 for d in [0, 1]])) for k in [j, j-1, i, i-1]])
        if math.exp((point1 - point2) / tlp) > random.random():
            travel = copy.copy(newTravel);
    helperX = [points[travel[i % pointCount]][0] for i in range(pointCount)]
    helperY = [points[travel[i % pointCount]][1] for i in range(pointCount)]

    print(l)
    if l < (len(restaurants) - 1):
        helperX.append(restaurants[l+1][0])
        helperY.append(restaurants[l+1][1])
    else:
        helperX.append(restaurants[0][0])
        helperY.append(restaurants[0][1])

    plt.plot(helperX, helperY, 'xb-');
    plt.show()