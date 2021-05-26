<h1 align="center">Edmonds Karp - Algorithm Implementation</h1>

<img src="https://img.shields.io/badge/python-3.9.1-green.svg">

Algorithm written for the subject Graph Theory related to the current course of study.

## Table of Content
- [Table of Content](#table-of-content)
- [About Algorithm](#about-algorithm)
- [Input format](#input-format)
- [Example Graph](#example-graph)

## About Algorithm
Edmonds-Karp algorithm is an implementation of the Ford-Fulkerson method that uses BFS for finding augmenting paths. Given a (network) graph which is just a set of verticies and directed edges with certain capacity. Algorithm tries to find maximum flow that can bu pushed from the source to the sink.  
More info about the algorithm you can be found [here](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm).

## Input format
```json
0, 5
[[0, 16, 13,  0,  0,  0],
 [0,  0, 10, 12,  0,  0],
 [0,  4,  0,  0, 14,  0],
 [0,  0,  9,  0,  0, 20],
 [0,  0,  0,  7,  0,  4],
 [0,  0,  0,  0,  0,  0]]
```
Algorithm reads input from the file (with .txt extension) which should be put in to [`graphs`](https://github.com/jwozn2k/EdmondsKarp/tree/main/graphs) folder.  
Format of the file is as folows:  
- First two digits separated by a coma are number of a source and sink node in the network.
- Then 2D adjacency matrix that represents maximum capacity of the edge between two vertices. (Zero means that there is no edge between two nodes).  

## Example Graph

  
