from galogic import *
import matplotlib.pyplot as plt
import progressbar
pbar = progressbar.ProgressBar()

for i in range(numNodes):
    RouteManager.addDustbin(Dustbin())

random.seed(seedValue)
yaxis = []
xaxis = []

pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print ('Initial minimum distance: ' + str(globalRoute.getDistance()))

for i in pbar(range(numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

print ('Global minimum distance: ' + str(globalRoute.getDistance()))

print ('Final Route: ' + globalRoute.toString())

xaxisPoint = []
yaxisPoint = []
for i in range(len(globalRoute.base)):
    xaxisPoint.append(globalRoute.base[i].x)
    yaxisPoint.append(globalRoute.base[i].y)

plt.plot(xaxis, yaxis, 'r-')
plt.show()
