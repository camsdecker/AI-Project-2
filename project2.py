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

        newtarget.walk()

        if victory(newagent, newtarget):
            break

        path = shortestpath(newagent.node, newtarget.node)
        newagent.followpath(path)
        steps = steps + 1

        if victory(newagent, newtarget):
            break
        
        
    #debugprint(newgraph, newagent, newtarget)
    return steps

# same as agent 1, except it moves to the closest space that the target can move to next
# this is unless the target is 1 space away, in which case the agent just moves right to it
def agent2():

    steps = 0       # number of steps it's taken to reach the target
    
    newgraph = graph.construct()
    newagent = agent(newgraph)
    newtarget = agent(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:
        
        #debugprint(newgraph, newagent, newtarget)
        #print("------------------------------------------")

        newtarget.walk()

        if victory(newagent, newtarget):
            break
        
        path = shortestpath(newagent.node, newtarget.node.edge1)    # this is where we find the closest space that the target may move to next turn...

        path2 = shortestpath(newagent.node, newtarget.node.edge2)
        if len(path2) < len(path):
            path = path2

        if newtarget.node.edge3 != -1:
            path3 = shortestpath(newagent.node, newtarget.node.edge3)
            if len(path3) < len(path):
                path = path3                                        

        if len(path) == 0:
            path = shortestpath(newagent.node, newtarget.node)      # if the agent is one space away from the target, it just moves directly to it to win

        newagent.followpath(path)
        steps = steps + 1

        if victory(newagent, newtarget):
            break
        
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
        #debugprint(newgraph, newagent, newtarget)
        if examine(newtarget, newgraph[0]):
            break
        newtarget.walk()
        steps = steps + 1
    #debugprint(newgraph, newagent, newtarget)
    return steps

# finds the highest probability that the target moves to node assuming that it's at one of node's neighbors
# according to our transition model, as long as the target is at a neighbor of x (x') then the probability that
# the target moves to x is 1 / # of neighbors of x', which will be 1/2 if any neighbor only has two edges (best case) or 1/3 if no neighbor has only two edges (worst case)
def neighborsprob(node):
    if node.edge1.edge3 == -1:
        return 1.0 / 2.0
    if node.edge2.edge3 == -1:
        return 1.0 / 2.0
    if node.edge2.edge3 == -1:
        return 1.0 / 2.0
    return 1.0/3.0

# returns list of the node's neighbors
def neighbors(node):
    neighbors = []
    neighbors.append(node.edge1)
    neighbors.append(node.edge2)
    if node.edge3 != -1:
        neighbors.append(node.edge3)
    return neighbors

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

# this function finds the highest possible probability that the target is at x at time t given our evidence y
def v(evidence, graph, returnnodes):
    t = len(evidence)   # t = current time step
    if t == 0:  # P(X0 = x) = 1 / total # of nodes
        return 1.0 / 40.0
    
    y = evidence.pop(0) # gives us Yt, AKA our observation at time t
    highestprob = 0    # highest probability that target is in node
    nodes = []   # list of nodes with highest probability of containing target

    for x in graph:
        #print(x)
        if y == x:  # if x == y, that means that we know for sure that the target wasn't at node x at this time step
            highestprob = 0
            continue
        currentprob = v(evidence, neighbors(x), 0) * neighborsprob(x)     # viterbi's algorithm
        #print(currentprob)
        if currentprob == highestprob:
            nodes.append(x)
        elif currentprob > highestprob:
            nodes = []
            nodes.append(x)
            highestprob = currentprob
    if returnnodes == 0:
        return highestprob
    else:
        return nodes

def chooserandom(nodes):
    index = random.randrange(0, len(nodes))
    return nodes[index]

# uses Viterbi's algorithm to find the most likely
def agent4():

    steps = 0       # number of steps it's taken to reach the target
    
    newgraph = graph.construct()
    #newagent = agent(newgraph)
    newtarget = agent(newgraph)

    evidence = []   # list containing each observation (Yt)
    curr = chooserandom(newgraph)

    # terminates after victory or 999 steps (arbitrary) to break out of potentially infinite loops
    while steps < 999:

        #debugprintfull(newgraph, newtarget, newtarget)

        #print("-----------Examining", curr.num)

        #debugprint(newgraph, newtarget, newtarget)
        
        if examine(newtarget, curr):  # breaks if we found the node (victory), else adds the node to the list of observations
            break
        else:
            evidence.insert(0, curr)
        newtarget.walk()
        steps = steps + 1

        copiedevidence = copy.deepcopy(evidence)
        nodes = v(copiedevidence, newgraph, 1)
        curr = chooserandom(nodes)
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

    
def printagent(agent, tries, avg, starttime):
    
    timetaken = time.clock_gettime(time.CLOCK_REALTIME) - starttime

    print("")
    print("Agent",agent)
    print(avg, "steps on average")
    #print("Total time:", timetaken, "seconds")
    print("Average time:", timetaken/tries, "seconds/iteration")
    print("")

def main():

    #newgraph = graph.construct()
    #evidence = [newgraph[0], newgraph[20], newgraph[36]]
    #nodes = v(evidence, newgraph, 1)
    #print(nodes)
    # redirects print() to out.txt
    
    f = open('out.txt', 'w')
    sys.stdout = f
    
    #agent4()

    runagents(1000)

main()