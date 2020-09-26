# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:29:59 2020

@author: 86156
"""

from network import network
from tree import tree

# activity on vertex for a directed acyclic network
def AOV(g):
    '''
    activity on vertex:
        to work out the sequence of doing tasks
        firstly, choose the vertexes whose indegree are 0
        indegree = 0 means you can do the task with out doing other tasks beforehand
        when finished one task, all the indegree of its adjacent vertexes should minus 1
        find the next vertexes whose indegree are 0 until all vertexes has been visited
    '''
    if isinstance(g, network) == False:
        print('ERROR: please input a directed acyclic network!')
        return -1
    if g.mark not in ['dg','dn']:
        print('ERROR: please input a directed acylic network!')
        return -1
    # initialization
    indegree = []
    for i in range(len(g.adjMat)):
        ind = 0
        for j in range(len(g.adjMat)):
            if g.adjMat[j][i] != g._network__INFINITY:
                ind += 1
        indegree += [ind]
    # main part
    count = 0
    sequence = []
    while count < len(g.vertexes):
        try:
            task = indegree.index(0)
            sequence.append(task)
            indegree[task] = -1
            count += 1
            for i in range(len(g.adjMat)):
                if g.adjMat[task][i] != g._network__INFINITY and indegree[i] != -1:
                    indegree[i] -= 1
        except:
            print('ERROR: there is a circle in the network, please check!')
            return -1
    return sequence
    

# find the critical path(activity on edge) 
# for a directed acyclic network which also has a source and a counter
def criticalPath(g):
    '''
    activity on edge:
        to find the critical path of a directed acyclic network with a source and a counter
        find the sequence of the tasks using the way used in AOV(activity on vertex)
        when visiting a vertex, count the least cost and save it
            the least cost is the maximum cost of all the routes from source to the vertex
        go from the counter to the source, count the maximum cost
            the maximum cost equals the maximum cost of its adjacent vertex minus the weight of arch
            if a vertex has more than one adjacent vertex 
            the maximum cost is the minimum of all the maximum costs
        critical vertex is a vertex whose least cost equals maximum cost
    '''
    if isinstance(g, network) == False:
        print('ERROR: please input a directed acyclic network which has a source and a counter!')
        return
    # find the source and the counter
    counter = []
    for i in g.adjMat:
        if i.count(g._network__INFINITY) == len(i):
            counter.append(i)
    if len(counter) == 0:
        print('ERROR: there is no counter in the network!')
        return
    if len(counter) > 1:
        print('ERROR: there are more than one counter! please make sure there is only one counter!')
        print('to meet this requirment, you can add a new vertex as the counter and \
              add arches with 0 weight from the old counters to the new vertex')
        return
    counter = counter[0]
    source = []
    for i in range(len(g.adjMat)):
        flag = 0
        for j in range(len(g.adjMat)):
            if g.adjMat[j][i] != g._network__INFINITY:
                flag = -1
                break
        if flag == 0:
            source.append(i)
    if len(source) == 0:
        print('ERROR: there is no source in the network!')
        return
    if len(source) > 1:
        print('ERROR: there are more than one source! please make sure there is only one source!')
        print('to meet this requirment, you can add a new vertex as the source and \
              add arches with 0 weight from the new vertex to the old sources') 
        return
    source = source[0]
    sequence = AOV(g)
    if sequence == -1:
        return
    leastCost = []
    maxCost = []
    for i in range(len(g.vertexes)):
        leastCost.append(0)
        maxCost.append(0)
    # main part
    for i in range(1, len(g.vertexes)):
        leastCost[i] = 0
        for j in range(i):
            if leastCost[i] < leastCost[j] + g.adjMat[sequence[j]][sequence[i]] \
            and g.adjMat[sequence[j]][sequence[i]] != g._network__INFINITY:         
                leastCost[i] = leastCost[j] + g.adjMat[sequence[j]][sequence[i]]
    maxCost[-1] = leastCost[-1]
    i = len(g.vertexes) - 2
    while i > 0:
        maxCost[i] = g._network__INFINITY
        for j in range(i+1, len(g.vertexes)):
            if maxCost[i] > maxCost[j] - g.adjMat[sequence[i]][sequence[j]] \
            and g.adjMat[sequence[i]][sequence[j]] != g._network__INFINITY:
                maxCost[i] = maxCost[j] - g.adjMat[sequence[i]][sequence[j]]
        i -= 1
    for i in range(len(sequence)):
        if maxCost[i] == leastCost[i]:
            print('(',g.vertexes[sequence[i]], end = '*)')
        else:
            print(g.vertexes[sequence[i]], end = '')

# Prim algorith(greedy algorithm)
# work out the minimum spanning tree for a connected network or strongly connected network
# minimum spanning tree is a tree that connects all the vertexes with the least total cost
# when used for a strongly connected network, 
# a root(a vertex from which can get to any other vertexes) should be selected first. 
# when used for a connected network, any vertex can be used as a root 
def PrimAlgorithm(g, root):
    '''
    Prim algorithm
        Prim algorithm is a kind of greedy algorithm
        the essence of Prim algorithm is to add vertexes into tree 
        until all vertexes have been added
        it is a way to find the minimum spanning tree of a (strongly) connected network
    '''
    if isinstance(g, network) == False:
        print('please input a connected/strongly connected network!')
        return
    if g.mark in ['ug','dg']:
        print('please input a connected/strongly connected network!')
        return
    mst = tree()
    mst.root = mst.makeNode()
    mst.nodes[mst.root].value = root
    usedVertexes = [root]
    cost = 0
    while len(usedVertexes) != len(g.vertexes):
        minDist = g._network__INFINITY
        parent = -1
        child = -1
        for e in set(g.vertexes).difference(set(usedVertexes)):
            for s in usedVertexes:
                if g.adjMat[g._network__locate(s)][g._network__locate(e)] < minDist:
                    parent = s
                    child = e
                    minDist = g.adjMat[g._network__locate(s)][g._network__locate(e)]
        if parent == -1:
            print('ERROR: the network is not a connected network!')
            print('or the root is not the right root for a strongly connected network!')
            return
        cost += minDist
        usedVertexes.append(child)
        childAdd = mst.makeNode()
        parentAdd = mst.Find(parent)
        mst.nodes[childAdd].value = child
        newChild = mst.nodes[parentAdd].lchild
        if newChild == -1:
            mst.nodes[parentAdd].lchild = childAdd
            mst.nodes[childAdd].parent = parentAdd
        else:
            while mst.nodes[newChild].rchild != -1:
                newChild = mst.nodes[newChild].rchild
            mst.nodes[newChild].rchild = childAdd
            mst.nodes[childAdd].parent = newChild
    print('the minimum cost is :', cost)
    print('minimum spanning tree is as following:')
    mst.Show()

# Kruskal algorithm(greedy algorithm)
# minimum spanning tree for a connected network
def KruskalAlgorithm(g):
    '''
    Kruskal algorithm
        Kruskal algorithm is a way of using greedy algorithm 
        to find the minimum spanning tree of a connected network.
        The essence of this algorithm is to add arched into the mst 
        until all vertexes have been added
    '''
    if isinstance(g, network) == False:
        print('ERROR: please input a connected network!')
        return
    if g.mark in ['dg','ug']:
        print('ERROR: please input a connected network!')
        return
    mst = tree()
    vertexGroup = list(range(len(g.vertexes)))
    usedVertexes = []# used for showing the tree 
    vertexesAdd = []# used for showing the tree
    for i in range(len(g.vertexes)):
        usedVertexes.append(0)
        vertexesAdd.append(-1)
    cost = 0
    while len(set(vertexGroup)) > 1:
        minDist = g._network__INFINITY
        s = 0
        e = 0
        for i in range(len(g.vertexes)):
            for j in range(len(g.vertexes)):
                if g.adjMat[i][j] < minDist and vertexGroup[i] != vertexGroup[j]:
                    minDist = g.adjMat[i][j]
                    s = i
                    e = j
        if minDist == g._network__INFINITY:
            print('ERROR: the network is not a connected network!')
            return
        # be careful here !
        # when a vertex is set to a new group 
        # all the vertexes that belong to the same group with this vertex should be included, too
        target = vertexGroup[s]
        origin = vertexGroup[e]
        for i in range(len(vertexGroup)):
            if vertexGroup[i] == origin:
                vertexGroup[i] = target
        if mst.root == -1:
            mst.root = mst.makeNode()
            mst.nodes[mst.root].value = g.vertexes[s]
            usedVertexes[mst.root] = 1
            vertexesAdd[mst.root] = mst.root
        if usedVertexes[s] == 0:
            parentAdd = mst.makeNode()
            mst.nodes[parentAdd].value = g.vertexes[s]
            vertexesAdd[s] = parentAdd
            usedVertexes[s] = 1
        if usedVertexes[e] == 0:
            childAdd = mst.makeNode()
            mst.nodes[childAdd].value = g.vertexes[e]
            vertexesAdd[e] = childAdd
            usedVertexes[e] = 1
        childAdd = vertexesAdd[e]
        parentAdd = vertexesAdd[s]
        newChild = mst.nodes[parentAdd].lchild
        if newChild == -1:
            mst.nodes[parentAdd].lchild = childAdd
            mst.nodes[childAdd].parent = parentAdd    
        else:
            while mst.nodes[newChild].rchild != -1:
                newChild = mst.nodes[newChild].rchild
            mst.nodes[newChild].rchild = childAdd
            mst.nodes[childAdd].parent = newChild
        cost += minDist
    print('the minimum cost is :', cost)
    print('minimum spanning tree is as following:')
    mst.Show()

# Dijkstra algorithm(dynamic programming)
# (shortest path)
def DijkstraAlgorithm(g, s):
    '''
    Dijkstra algorithm
        Dijkstra algorithm is a way of using dynamic programming 
        to find the shortest path from a vertex to any other vertexes it can connected with
        it can be used for a directed network/graph or an undirected network/graph
    '''
    if isinstance(g, network) == False:
        print('ERROR: please input a network!')
        return
    pos = g._network__locate(s)
    if pos == -1:
        print('ERROR: vertex not found in the network!')
        return
    cost = []
    route = []
    # cost[e] is the length of the shortest path from s to e
    # route[e] is the specific route of the shortest path from s to e
    for i in range(len(g.vertexes)):
        cost.append(g._network__INFINITY)
        route.append('null')
    cost[pos] = 0
    route[pos] = s 
    usedVertexes = [s]
    # dynamic programming
    while len(usedVertexes) != len(g.vertexes):
        minCost = g._network__INFINITY
        start = s
        end = s
        for m in set(g.vertexes).difference(set(usedVertexes)):
            for i in usedVertexes:
                if cost[g._network__locate(m)] >= cost[g._network__locate(i)] + \
                            g.adjMat[g._network__locate(i)][g._network__locate(m)]:
                    cost[g._network__locate(m)] = cost[g._network__locate(i)] + \
                            g.adjMat[g._network__locate(i)][g._network__locate(m)]
                    if minCost > cost[g._network__locate(m)]:
                        start = i
                        end = m
                        minCost = cost[g._network__locate(m)]
        if minCost == g._network__INFINITY:
            print('Warning: not all vertexes can be reached from the vertex', s)
            print('vertexes can be reached:')
            print(usedVertexes)
            print('routes are as following:')
            print(route)
            print('length are as following:')
            print(cost)
            return cost, route
        cost[g._network__locate(end)] = cost[g._network__locate(start)] + \
                                        g.adjMat[g._network__locate(start)][g._network__locate(end)]
        route[g._network__locate(end)] = route[g._network__locate(start)] + end
        usedVertexes.append(end)
    return cost, route

# Floyd algorithm(dynamic programming)
# (shortest path)
def FloydAlgorithm(g):
    '''
    Floyd algorithm
        Floyd algorithm is a way of using dynamic programming
        to find all the shortest path from a vertex to a nother vertex in a network
        it can be used for a directed network/graph or an undirected network/graph
    '''
    if isinstance(g, network) == False:
        print('ERROR:please input a network!')
        return
    cost = []
    route = []
    # cost[s][e] is the length of the shortest path from s to e
    # route[s][e] is the specific route of the shortest path from s to e
    for i in range(len(g.vertexes)):
        cost.append([g.adjMat[i][0]])
        if g.adjMat[i][0] != g._network__INFINITY:
            route.append([g.vertexes[i] + g.vertexes[0]])
        else:
            route.append(['null'])
        for j in range(1, len(g.vertexes)):
            cost[i].append(g.adjMat[i][j])
            if g.adjMat[i][j] != g._network__INFINITY:
                route[i].append(g.vertexes[i] + g.vertexes[j])
            else:
                route[i].append('null')
        cost[i][i] = 0
        route[i][i] = g.vertexes[i]
    # dynamic programming
    for m in range(len(g.vertexes)):
        for s in range(len(g.vertexes)):
            for e in range(len(g.vertexes)):
                if cost[s][m] + cost[m][e] < cost[s][e]:
                    cost[s][e] = cost[s][m] + cost[m][e]
                    route[s][e] = route[s][m] + route[m][e][1:]
    # show the result
    def showMat(Mat, title, disable):
        print('   ', end = '')
        for i in range(len(Mat)):
            print(title[i], '   ', end = '')
        print('')
        for i in range(len(Mat)):
            print(title[i], ' ', end = '')
            for j in range(len(Mat)):
                if Mat[i][j] == disable:
                    print('--- ', end = '')
                else:
                    print(Mat[i][j], ' ', end = '')
            print('')
    print('the length of shortest paths are as following (row is the tail, column is the head): ')
    showMat(cost, g.vertexes, g._network__INFINITY)
    return cost, route