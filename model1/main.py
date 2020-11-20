import cv2

class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)


def aStar(maze, start, end):

    startNode = Node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0

    openList = []
    closedList = set()

    openList.append(startNode)

    while len(openList) > 0:

        currentNode = openList[0]
        currentIndex = 0
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        openList.pop(currentIndex)
        closedList.add(currentNode)

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        newWay = []
        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            if nodePosition[0] > (len(maze) - 1) or nodePosition[0] < 0 or nodePosition[1] > (len(maze[len(maze)-1]) -1) or nodePosition[1] < 0:
                continue

            if maze[nodePosition[0]][nodePosition[1]] != 0:
                continue

            newNode = Node(currentNode, nodePosition)

            newWay.append(newNode)

        for way in newWay:

            if way in closedList:
                continue

            way.g = currentNode.g + 1
            way.h = ((way.position[0] - endNode.position[0]) ** 2) + ((way.position[1] - endNode.position[1]) ** 2)
            way.f = way.g + way.h

            for openNode in openList:
                if way == openNode and way.g > openNode.g:
                    continue

            openList.append(way)
def main():
    img = cv2.imread("problem.bmp")
    height, width, channels = img.shape

    blue = "[255   0   0]"
    red = "[  0   0 255]"
    black = "[0 0 0]"
    white = "[255 255 255]"
    mazeHelp = []
    maze = []


    for i in range(width):
        for j in range(height):
            if (str(img[i, j]) in white):
                mazeHelp.append(0)
            if (str(img[i, j]) in black):
                mazeHelp.append(1)
            if (str(img[i, j]) in red):
                mazeHelp.append(0)
                start = (i, j)
            if (str(img[i, j]) in blue):
                mazeHelp.append(0)
                end = (i, j)
        maze.append(mazeHelp)
        mazeHelp = []
    path = aStar(maze, start, end)

    for k in path:
        img[k] = [0, 255, 255]
    cv2.imwrite('result.bmp', img)
    print("Total cost:")
    print(len(path))
    print("The path:")
    return path

print(main())


