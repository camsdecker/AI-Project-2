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

    # constructs a playing field for the agents and target
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
            while num2 == num: # repeatedly rerolls second random number if it's the same as first
                num2 = random.randrange(40)

            if graph[num].edge2 == -1:
                graph[num].edge2 = graph[num2]
            elif graph[num].edge3 == -1:
                graph[num].edge3 = graph[num2]
            else:
                i = i - 1

            i = i + 1
        return graph

def debugprint(graph, agent, target):
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

        if target.node == x:
            print("(TARGET HERE!!!)")
        if agent.node == x:
            print("(AGENT HERE!!!)")

        print("")
class target():
    def __init__(self, graph):
        self.node = graph[random.randrange(0,40)]        # target is initialized/starts at random node

    # randomly moves the target to a different neighboring node
    def walk(self):
        # finds how many edges the current node has and randomly moves it to one of them
        if self.node.edge3 != -1:       # 3 edges
            num = random.randrange(0,3)
            if num == 0:
                self.node = self.node.edge1
            elif num == 1:
                self.node = self.node.edge2
            else:
                self.node = self.node.edge3
        elif self.node.edge2 != -1:     # 2 edges
            if random.randrange(0,2):
                self.node = self.node.edge1
            else:
                self.node = self.node.edge2
        else:                           # 1 edge
            self.node = self.node.edge1
        
        return

# checks if the agent is in the same node as the target and returns 1 if victorious and 0 if not
def checkvictory(agent,target):
    if agent.node == target.node:
        return 1
    return 0

def agent0():

    steps = 0       # number of steps it's taken to reach the target
    victory = 0     # whether the agent has reached the target
    
    newgraph = graph.construct()
    newagent = target(newgraph)
    newtarget = target(newgraph)

    while not victory:

        debugprint(newgraph, newagent, newtarget)

        newtarget.walk()
        victory = checkvictory(newagent, newtarget)
        steps = steps + 1
    debugprint(newgraph, newagent, newtarget)
    return steps

def main():

    # redirects print() to out.txt
    f = open('out.txt', 'w')
    sys.stdout = f

    agent0()
main()