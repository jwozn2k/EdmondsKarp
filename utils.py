
def read_from_the_file(fileName: str):
    """
    Function read input from the file

    Parameters:
    arg1 (string): Name of the file that function will read from

    Return:
    tuple: (adjacency matrix, start, sink)
        - adjacency matrix stores capacities of edges between two nodes
        - start is index of a source node
        - sink is index of a sink node
    """
    capacities = list()

    with open(fileName, 'r') as file:
        # read start and sink node
        firstLine = file.readline().strip()
        numOfNodes, start, sink = firstLine.split(",")

        # read capacities to an array
        for line in file:
            row = list()
            line = line[:-2]
            line = line.replace("[", "").replace("]", "")

            for capacity in line.strip().split(","):
                row.append(int(capacity))

            capacities.append(row)

    # check if rows == columns and raise an exception if is not

    return capacities, start, sink