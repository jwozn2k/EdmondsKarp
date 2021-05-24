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

    # try to read from the file
    try:
        with open(fileName, 'r') as file:
            # read number of nodes, start and sink node
            firstLine = file.readline().strip()
            start, sink = firstLine.split(",")
            start, sink = int(start), int(sink)

            # read capacities to an array
            for line in file:
                row = list()
                line = line[:-2]
                line = line.replace("[", "").replace("]", "")

                for capacity in line.strip().split(","):
                    row.append(int(capacity))

                capacities.append(row)

            numOfNodes = len(capacities)
            if start < 0 or sink > numOfNodes - 1:
                raise Exception("Wrong index of start or sink node!")

    except IOError:
        raise Exception("Wrong file name. Try again!")


    # check if rows == columns and raise an exception if is not
    if len(capacities) != len(capacities[0]):
        raise Exception(f"You should pass square array in {fileName} file")

    return capacities, start, sink
