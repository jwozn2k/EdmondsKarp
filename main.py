from utils import read_from_the_file
import sys

def BelmandFord(capacities: list, start: int, sink: int):
    """ Function returns maximum flow that can be obtain in the network """
    residualCapacity = [row for row in capacities]
    augmentedPaths = list()
    maxFlow = 0
    while True:
        foundAugmentedPath, parent = BFS(residualCapacity, start, sink)

        # we are looping untill there is any augmenting path
        if not foundAugmentedPath:
            break

        path = list()
        currentFlow = sys.maxsize
        node = sink
        # Find bottleneck value (minimum capacity of the edge) on this path
        # Moving backward from sink to start node
        while node != start:
            path.append(node)
            v = parent[node]
            if residualCapacity[v][node] < currentFlow:
                currentFlow = residualCapacity[v][node]
            node = v

        # Add path to the augmented paths and update max_flow
        path.append(start)
        augmentedPaths.append(path[::-1])
        maxFlow += currentFlow

        # Update values of the edges, subtract flow to the forward edges
        # and add flow from the backward edges
        node = sink
        while node != start:
            v = parent[node]
            residualCapacity[v][node] -= currentFlow
            residualCapacity[node][v] += currentFlow
            node = v

    print("------AUGMENTED PATHS------")
    for index, path in enumerate(augmentedPaths):
        print(f"{index + 1} path: {path}")

    return maxFlow

def BFS(residualCapacity: list, start: int, sink: int):
    """ Function is looing for an augmenting path and returns one if found """
    # Initialization of data structures
    visited = set()
    queue = list()
    parent = dict()

    # We always start from source node
    queue.append(start)
    visited.add(start)
    foundAugmentedPath = False
    numOfNodes = len(residualCapacity)

    # Loop untill queue is not empty
    while len(queue) > 0:
        current = queue.pop()

        # find out where we can go from current node
        for v in range(numOfNodes):
            # we can visit only these nodes that haven't been already visited
            # and go through an edge which residualCapacity is grater that zero
            if v not in visited and residualCapacity[current][v] > 0:
                parent[v] = current
                visited.add(v)
                queue.append(v)
                # stop BFS as soon as sink node is reached
                if v == sink:
                    foundAugmentedPath = True
                    break

    return foundAugmentedPath, parent

if __name__ == "__main__":
    fileName = input("File name to read the input from: ")
    matrix, s, t = read_from_the_file("graphs/" + fileName)
    maxFlow = BelmandFord(matrix, s, t)
    print("Maximum flow in this network: ", maxFlow)