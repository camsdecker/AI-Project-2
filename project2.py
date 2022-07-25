import sys
import random
import math
import time
import copy
import numpy

class node(object):
    def __init__(self):
        self.num = -1
        self.edge1 = -1
        self.edge2 = -1
        self.edge3 = -1

# returns a new graph
class graph():
    def construct():
        graph = []

        # adds verteces
        for i in range(40):
            graph.append(node())
            graph[i].num = i
            graph[i-1].edge1 = graph[i]
        graph[39].edge1 = graph[0]
        
        i = 0

        while i < 10:
            num = random.randrange(40)
            num2 = random.randrange(40)
            while num2 == num: # rerolls second random number if it's the same as first
                num2 = random.randrange(40)

            if graph[num].edge2 == -1:
                graph[num].edge2 = graph[num2]
            elif graph[num].edge3 == -1:
                graph[num].edge3 = graph[num2]
            else:
                i = i - 1

            i = i + 1
        return graph

    def print(graph):
        for x in graph:
            print("Node:", x.num)
            if x.edge1 != -1:
                print("Edge 1:", x.edge1.num)
            else:
                print("Edge 1: n/a")
            if x.edge2 != -1:
                print("Edge 2:", x.edge2.num)
            else:
                print("Edge 2: n/a")
            if x.edge3 != -1:
                print("Edge 3:", x.edge3.num)
            else:
                print("Edge 3: n/a")
            print("")

def main():
    newgraph = graph.construct()
    graph.print(newgraph)
main()