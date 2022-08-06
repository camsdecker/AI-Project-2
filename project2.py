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
        self.prob = 1.0 / 40.0
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
            #print("NUM (3 edges:)", num)
            if num == 0:
                self.node = self.node.edge1
            elif num == 1:
                self.node = self.node.edge2
            else:
                self.node = self.node.edge3
        else:
            num = random.randrange(0,2)
            #print("NUM (2 edges:)", num)
            if num == 0:
                self.node = self.node.edge1
            elif num == 1:
                self.node = self.node.edge2
        
        return

    # moves the agent one step along the path
    # returns 1 if successful, 0 if not
    def followpath(self, path):
        if not path:
            return 0
        next = path.pop(0)

        if next == self.node.edge1 or next == self.node.edge2 or next == self.node.edge3:
            self.node = next
            return 1
        return 0

def debugprintfull(graph, agent, target):
    for x in graph:

        print("Node:", x.num)
        print("Probability:", x.prob)
        
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
    print("Probability:", x.prob)

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
    print("Probability:", x.prob)

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

def findpath(S, G):
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
            newpath.insert(0,current.edge1)
            fringe.append(newpath)
            if current.edge2 != -1:
                newpath = list(path)
                newpath.insert(0,current.edge2)
                fringe.append(newpath)
                if current.edge3 != -1:
                    newpath = list(path)
                    newpath.insert(0,current.edge3)
                    fringe.append(newpath)
            
            closed.append(current)
    #print("Search completed in", time.clock_gettime(time.CLOCK_REALTIME) - starttime, "seconds (fail)")
    return 0

# checks if the agent is in the same node as the target and returns 1 if victorious and 0 if not
# maybe unnecessary but makes the code easier to read imo
def victory(agent,target):
    if agent.node == target.node:
        return 1
    return 0

# examines a node, returning 1 if the target is at that node and 0 if not
def examine(target, node):
    if node == target.node:
        return 1
    else:
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
        if victory(newagent, newtarget):
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

        #newtarget.walk()

        path = findpath(newagent.node, newtarget.node)
        newagent.followpath(path)
        steps = steps + 1

        if victory(newagent, newtarget):
            break

        newtarget.walk()
        
        
    #debugprint(newgraph, newagent, newtarget)
    return steps

# uses a BFS to find the shortest path to the target
def agent2():   # FIXME

    steps = 0       # number of steps it's taken to reach the target
    
    newgraph = graph.construct()
    newagent = agent(newgraph)
    newtarget = agent(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:
        
        #debugprint(newgraph, newagent, newtarget)
        #print("------------------------------------------")

        #newtarget.walk()

        path = shortestpath(newagent.node, newtarget.node)
        newagent.followpath(path)
        steps = steps + 1

        if victory(newagent, newtarget):
            break

        newtarget.walk()
        
        
    #debugprint(newgraph, newagent, newtarget)
    return steps

# examines node 0 at every step until target is at node
def agent3():

    steps = 0       # number of steps it's taken to reach the target
    
    newgraph = graph.construct()
    #newagent = agent(newgraph)
    newtarget = agent(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:
        # agent's turn
        if examine(newtarget, newgraph[0]):
            break

        # targets turn
        newtarget.walk()
        steps = steps + 1

    return steps

# returns list of the node's neighbors
def neighbors(node):
    neighbors = []
    neighbors.append(node.edge1)
    neighbors.append(node.edge2)
    if node.edge3 != -1:
        neighbors.append(node.edge3)
    return neighbors

# chooses a random node from a list of nodes
def chooserandom(nodes):
    index = random.randrange(0, len(nodes))
    return nodes[index]

# compiles a list of nodes with the nodes most likely to contain the target, then returns a random node from among them
def mostlikely(graph):
    nodes = []  # list containing highest probability nodes
    highest = 0     # highest probability
    for x in graph:
        if x.prob == 0:
            continue

        if x.prob == highest:
            nodes.append(x)
        elif x.prob > highest:
            highest = x.prob
            nodes = []
            nodes.append(x)
    return chooserandom(nodes)

# compiles a list of nodes with the nodes that are the second most likely to contain the target
def secondmostlikely(graph):
    exclude = []    # first we make a list of nodes with highest probability, then start over and ignore the highest probability nodes
    highest = 0     # highest probability
    for x in graph:
        if x.prob == 0:
            continue

        if x.prob == highest:
            exclude.append(x)
        elif x.prob > highest:
            highest = x.prob
            exclude = []
            exclude.append(x)

    nodes = []  # list containing second highest probability nodes
    highest = 0     # second highest probability
    for x in graph:
        if x in exclude:    # ignore the nodes with highest probability
            continue
        if x.prob == 0:
            continue

        if x.prob == highest:
            nodes.append(x)
        elif x.prob > highest:
            highest = x.prob
            nodes = []
            nodes.append(x)
    if len(nodes) == 0:
        return chooserandom(graph)
    return chooserandom(nodes)

#Initial Distribution:
#P(X0 = x) = 1 / total # of nodes
#
#Transition model:
#P(Xt+1 = x | Xt = x' (where x' is not adjacent to x)) = 0
#P(Xt+1 = x | Xt = x' (where x' is adjacent to x)) = 1 / # of neighbors of x'
#
#Observation model:
#P(Yt = target not at x | Xt = x) = 0
#P(Yt = target not at x | Xt = x') = 1

# x is a node that we want to get calculate the chance of containing the target
# observation represents the last node that we've observed and know doesn't contain the target
def belief(graph):
    for x in graph:
        prob = 0

        for xprime in neighbors(x):     # we'll only evaluate neighbors of x, since it'll be 0 otherwise
            prob += xprime.prob * (1.0 / len(neighbors(xprime)))    # Belief(x)

        x.prob = prob
    return

# uses filtering to find the node most likely to contain the target
def agent4():
    steps = 0       # number of steps it's taken to reach the target
    newgraph = graph.construct()
    newtarget = agent(newgraph)
    curr = mostlikely(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:
        #debugprintfull(newgraph, newtarget, newtarget)
        # agent's turn
        curr = mostlikely(newgraph)     # examines most probable node
        if curr == newtarget.node:  # breaks if we found the node (victory), otherwise we assume the target is not at the observed node
            break
        else:
            curr.prob = 0
        belief(newgraph)    # updates probabilities of every node

        # target's turn
        newtarget.walk()
        steps = steps + 1

    return steps

def agent5():   #FIXME
    steps = 0       # number of steps it's taken to reach the target
    newgraph = graph.construct()
    newtarget = agent(newgraph)
    curr = mostlikely(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:
        #debugprintfull(newgraph, newtarget, newtarget)
        # agent's turn
        curr = secondmostlikely(newgraph)     # examines most probable node
        if curr == newtarget.node:  # breaks if we found the node (victory), otherwise we assume the target is not at the observed node
            break
        else:
            curr.prob = 0
        belief(newgraph)    # updates probabilities of every node

        # target's turn
        newtarget.walk()
        steps = steps + 1

    return steps

# examines the most probable node, updates belief state, then finds shortest path to new highest probability node
def agent6():
    steps = 0       # number of steps it's taken to reach the target
    newgraph = graph.construct()
    newagent = agent(newgraph)
    newtarget = agent(newgraph)
    curr = mostlikely(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:

        # agent's turn
        curr = mostlikely(newgraph)     # examines most probable node
        if curr == newtarget.node:  # updates probability of examined node containing target
            curr.prob = 1
        else:
            curr.prob = 0
        belief(newgraph)    # updates belief state

        path = shortestpath(newagent.node, mostlikely(newgraph))    # finds shortest path to new highest probability node
        newagent.followpath(path)

        if victory(newagent, newtarget):
            break

        # target's turn
        newtarget.walk()
        steps = steps + 1

    return steps

# returns a path to the closest node with the highest probability
def closestpath(graph, agent):
    nodes = []  # list containing highest probability nodes
    highest = 0     # highest probability
    for x in graph:
        if x.prob == 0:
            continue

        if x.prob == highest:
            nodes.append(x)
        elif x.prob > highest:
            highest = x.prob
            nodes = []
            nodes.append(x)

    bestpath = []
    for x in nodes:
        path = shortestpath(agent.node, x)
        if len(path) > len(bestpath):
            bestpath = path
    return bestpath

# like agent 6, except it chooses the node with highest probability that is closest to the agent
def agent7():   #FIXME
    steps = 0       # number of steps it's taken to reach the target
    newgraph = graph.construct()
    newagent = agent(newgraph)
    newtarget = agent(newgraph)
    curr = mostlikely(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:
        # agent's turn
        curr = mostlikely(newgraph)     # examines most probable node
        if curr == newtarget.node:  # updates probability of examined node containing target
            curr.prob = 1
        else:
            curr.prob = 0
        belief(newgraph)    # updates belief state

        path = closestpath(newgraph, newagent)    # finds shortest path to new highest probability node
        newagent.followpath(path)

        if victory(newagent, newtarget):
            break

        # target's turn
        newtarget.walk()
        steps = steps + 1

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

    # AGENT 2
    avg = 0     # the average number of steps taken for each agent
    
    starttime = time.clock_gettime(time.CLOCK_REALTIME)
    for i in range(tries):
        avg = avg + agent2()
    avg = avg / tries

    printagent(2, tries, avg, starttime)

    # AGENT 3
    avg = 0     # the average number of steps taken for each agent
    
    starttime = time.clock_gettime(time.CLOCK_REALTIME)
    for i in range(tries):
        avg = avg + agent3()
    avg = avg / tries

    printagent(3, tries, avg, starttime)

    # AGENT 4
    avg = 0     # the average number of steps taken for each agent
    
    starttime = time.clock_gettime(time.CLOCK_REALTIME)
    for i in range(tries):
        avg = avg + agent4()
    avg = avg / tries

    printagent(4, tries, avg, starttime)

    # AGENT 5
    avg = 0     # the average number of steps taken for each agent
    
    starttime = time.clock_gettime(time.CLOCK_REALTIME)
    for i in range(tries):
        avg = avg + agent5()
    avg = avg / tries

    printagent(5, tries, avg, starttime)

    # AGENT 6
    avg = 0     # the average number of steps taken for each agent
    
    starttime = time.clock_gettime(time.CLOCK_REALTIME)
    for i in range(tries):
        avg = avg + agent6()
    avg = avg / tries

    printagent(6, tries, avg, starttime)

    # AGENT 7
    avg = 0     # the average number of steps taken for each agent
    
    starttime = time.clock_gettime(time.CLOCK_REALTIME)
    for i in range(tries):
        avg = avg + agent7()
    avg = avg / tries

    printagent(7, tries, avg, starttime)

    
def printagent(agent, tries, avg, starttime):
    
    timetaken = time.clock_gettime(time.CLOCK_REALTIME) - starttime

    print("")
    print("Agent",agent)
    print(avg, "steps on average")
    #print("Total time:", timetaken, "seconds")
    print("Average time:", timetaken/tries, "seconds/iteration")
    print("")

def main():

    f = open('out.txt', 'w')
    sys.stdout = f

    runagents(10000)

main()