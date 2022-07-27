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
class graph():

    # constructs a playing field for the agents and target
    def construct():
        graph = []

        # adds verteces
        for i in range(40):
            graph.append(node())
            graph[i].num = i
            graph[i].edge1 = graph[i-1]
            graph[i-1].edge2 = graph[i]
        graph[39].edge1 = graph[38]
        graph[39].edge2 = graph[0]
        graph[0].edge1 = graph[39]
        
        i = 0

        while i < 10:
            num = random.randrange(40)
            num2 = random.randrange(40)
            while num2 == num: # repeatedly rerolls second random number if it's the same as first
                num2 = random.randrange(40)

            # checks if nodes are already connected
            if graph[num].edge1 == graph[num2] or graph[num].edge2 == graph[num2]:
                continue

            # checks if edge3 is empty
            if graph[num].edge3 == -1 and graph[num2].edge3 == -1:
                graph[num].edge3 = graph[num2]
                graph[num2].edge3 = graph[num]
            else:
                continue

            i = i + 1
        return graph
class agent():
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
        else:
            if random.randrange(0,2):
                self.node = self.node.edge1
            else:
                self.node = self.node.edge2
        
        return

    # moves the agent one step along the path
    # returns 1 if successful, 0 if not
    def followpath(self, path):
        next = path.pop(0)

        if next == self.node.edge1 or next == self.node.edge2 or next == self.node.edge3:
            self.node = next
            return 1
        return 0

def debugprintfull(graph, agent, target):
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

def debugprint(graph, agent, target):
    #for x in graph:

    x = agent.node

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

    x = target.node

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

# finds the shortest path from the agent's node (S) to the target's node (G) using BFS
def shortestpath(S, G):
    #starttime = time.clock_gettime(time.CLOCK_REALTIME)
    fringe = []
    closed = []
    fringe.append([S])
    while len(fringe) > 0:
        path = fringe.pop(0)
        current = path[-1]
        if current in closed:
            continue
        if current == G:
            #print("Search completed in", time.clock_gettime(time.CLOCK_REALTIME) - starttime, "seconds (success)")
            path.pop(0)
            return path
        else:
            newpath = list(path)
            newpath.append(current.edge1)
            fringe.append(newpath)
            if current.edge2 != -1:
                newpath = list(path)
                newpath.append(current.edge2)
                fringe.append(newpath)
                if current.edge3 != -1:
                    newpath = list(path)
                    newpath.append(current.edge3)
                    fringe.append(newpath)
            
            closed.append(current)
    #print("Search completed in", time.clock_gettime(time.CLOCK_REALTIME) - starttime, "seconds (fail)")
    return 0

# checks if the agent is in the same node as the target and returns 1 if victorious and 0 if not
def checkvictory(agent,target):
    if agent.node == target.node:
        return 1
    return 0

# sits at starting node and waits for target
def agent0():

    steps = 0       # number of steps it's taken to reach the target
    
    newgraph = graph.construct()
    newagent = agent(newgraph)
    newtarget = agent(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:
        #debugprint(newgraph, newagent, newtarget)
        if checkvictory(newagent, newtarget):
            break
        newtarget.walk()
        steps = steps + 1
    #debugprint(newgraph, newagent, newtarget)
    return steps

# moves toward target each step
def agent1():

    steps = 0       # number of steps it's taken to reach the target
    
    newgraph = graph.construct()
    newagent = agent(newgraph)
    newtarget = agent(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:
        
        #debugprint(newgraph, newagent, newtarget)
        #print("------------------------------------------")

        newtarget.walk()

        if checkvictory(newagent, newtarget):
            break

        path = shortestpath(newagent.node, newtarget.node)
        newagent.followpath(path)
        steps = steps + 1

        if checkvictory(newagent, newtarget):
            break
        
        
    #debugprint(newgraph, newagent, newtarget)
    return steps

# runs each agent and averages the number of steps it took to reach victory with a sample size of tries
def runagents(tries):
    
    print("Iterations:", tries)

    # AGENT 0
    avg = 0     # the average number of steps taken for each agent
    
    starttime = time.clock_gettime(time.CLOCK_REALTIME)
    for i in range(tries):
        avg = avg + agent0()
    avg = avg / tries

    printagent(0, tries, avg, starttime)

    # AGENT 1
    avg = 0     # the average number of steps taken for each agent
    
    starttime = time.clock_gettime(time.CLOCK_REALTIME)
    for i in range(tries):
        avg = avg + agent1()
    avg = avg / tries

    printagent(1, tries, avg, starttime)

    
def printagent(agent, tries, avg, starttime):
    
    timetaken = time.clock_gettime(time.CLOCK_REALTIME) - starttime

    print("")
    print("Agent",agent)
    print(avg, "steps on average")
    #print("Total time:", timetaken, "seconds")
    print("Average time:", timetaken/tries, "seconds/iteration")
    print("")

def main():

    # redirects print() to out.txt
    f = open('out.txt', 'w')
    sys.stdout = f
    
    runagents(1000)

main()