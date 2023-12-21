# Class to represent a graph
class MyGraph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, start, end, weight):
        self.graph.append([start, end, weight])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):

        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for start, end, weight in self.graph:
                if dist[start] != float("Inf") and dist[start] + weight < dist[end]:
                    dist[end] = dist[start] + weight

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if the graph doesn't contain
        # a negative-weight cycle. If we get a shorter path, then there
        # is a cycle.

        for start, end, weight in self.graph:
            if dist[start] != float("Inf") and dist[start] + weight < dist[end]:
                print("Graph contains a negative weight cycle")
                return

        # print all distances
        self.printArr(dist)


# Driver's code
if __name__ == '__main__':
    myGraph = MyGraph(6)
    myGraph.addEdge(0, 1, 2)
    myGraph.addEdge(0, 2, 4)
    myGraph.addEdge(1, 2, 1)
    myGraph.addEdge(1, 3, 7)
    myGraph.addEdge(2, 4, 3)
    myGraph.addEdge(3, 4, 1)
    myGraph.addEdge(3, 5, 5)
    myGraph.addEdge(4, 5, 2)

    # function call
    myGraph.BellmanFord(0)
