# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:47:50 2020

@author: 86156
"""

from Queue import Queue
from stack import Stack

class network():
    '''
    directed network:
        graph is a special kind of network in which all the weights on arches are 1
        undirected network is a special kind of directed network in which all the arches are bidirectional
        attribute:
            arch(tail->head)
            vertex
            weight
        basic methods:
            create a network
            destroy a network
            show a network
            traverse a network
            find the first adjacent vertex of a vertex
            find the next adjacent vertex of a vertex
            add a vertex into a network
            add an arch into a network
            delete an arch from a network
            delete a vertex from a network
            update the value of a vertex/arch of network
            find a simple path between two vertexes
        other methods:
            work out the minimum spanning tree of a connected network/strongly connected network
            find the shortest path between two vertexes
            activity on vertex/activity on edge for directed acyclic network
    '''
    
    __INFINITY = 32768
    
    def __init__(self):
        self.vertexes = []
        self.adjMat = []
        self.mark = 'dn'
        
    # get the location of a vertex
    def __locate(self, vertex):
        for pos in range(len(self.vertexes)):
            if self.vertexes[pos] == vertex:
                return pos
        return -1
    
    # add column and row in adjMat
    def __addColumnRow(self):
        length = len(self.adjMat)
        self.adjMat.append([self.__INFINITY])
        for i in range(length):
            self.adjMat[i].append(self.__INFINITY)
            self.adjMat[length].append(self.__INFINITY)

    def destroy(self):
        self.adjMat = []
        self.vertexes = []
        
    def create(self):
        print('which kind of network do you want to create?')
        self.mark = input("undirected graph:'ug', undirected network:'un',directed graph:'dg', directed network:'dn'")
        while True:
            s = input("please input the name of the tail vertex, input 'k' to end:")
            if s == 'k':
                return
            if s not in self.vertexes:
                self.vertexes.append(s)
                self.__addColumnRow()
            e = input("please input the name of the head vertex, input 'k' to end:")
            if e == 'k':
                return
            if e not in self.vertexes:
                self.vertexes.append(e)
                self.__addColumnRow()            
            choice = input("is there an arch between them? for yes input 'y', no input 'n':")
            if choice == 'y':
                if self.mark in ['ug','dg']:
                    w = 1
                else:                    
                    w = float(input('please input the weight of the arch:'))
            else:
                w = self.__INFINITY
            ps = self.__locate(s)
            pe = self.__locate(e)
            self.adjMat[ps][pe] = w
            if self.mark in ['ug', 'un']:
                self.adjMat[pe][ps] = w
               
    def show(self):
        print('   ', end = '')
        for i in range(len(self.adjMat)):
            print(self.vertexes[i], '   ', end = '')
        print('')
        for i in range(len(self.adjMat)):
            print(self.vertexes[i], ' ', end = '')
            for j in range(len(self.adjMat)):
                if self.adjMat[i][j] == self.__INFINITY:
                    print('--- ', end = '')
                else:
                    print(self.adjMat[i][j], ' ', end = '')
            print('')
        
    def firstAdj(self, v):
        pos = self.__locate(v)
        if pos == -1:
            return -1
        for i in range(len(self.adjMat)):
            if self.adjMat[pos][i] != self.__INFINITY:
                return self.vertexes[i]
        return -1
   
    def nextAdj(self, v, p):
        pos = self.__locate(v)
        posp = self.__locate(p)
        if pos == -1 or posp == -1:
            return -1
        if self.adjMat[posp][pos] == self.__INFINITY:
            return -1
        for i in range(pos + 1, len(self.adjMat)):
            if self.adjMat[posp][i] != self.__INFINITY:
                return self.vertexes[i]
        return -1
        
    def traverse(self, mode = 'd'):
        traversed = []
        def depthTraverse(self, index):
            if index == -1:
                return
            if index in traversed:
                return
            print(self.vertexes[index], end = '')
            traversed.append(index)
            tmp = self.firstAdj(self.vertexes[index])
            while tmp != -1:
                depthTraverse(self, self.__locate(tmp))
                tmp = self.nextAdj(tmp, self.vertexes[index])
        def breadthTraverse(self, index):
            if index == -1:
                return
            q = Queue()
            print(self.vertexes[index], end = '')
            traversed.append(index)
            q.insert(index)
            while q.empty() == False:
                p = self.vertexes[q.delete()]
                if self.firstAdj(p) == -1:
                    continue
                tmp = self.__locate(self.firstAdj(p))
                while tmp not in traversed:
                    print(self.vertexes[tmp], end = '')
                    traversed.append(tmp)
                    q.insert(tmp)
                    if self.nextAdj(self.vertexes[tmp], p) == -1:
                        break
                    tmp = self.__locate(self.nextAdj(self.vertexes[tmp], p))
        for i in range(len(self.vertexes)):
            if i not in traversed:            
                if mode == 'd':# traverse in depth first sequence
                    depthTraverse(self, i)
                else:# traverse in breadth first sequence
                    breadthTraverse(self, i)
    
    def addVertex(self, v):
        if self.__locate(v) != -1:
            print('ERROR: vertex already in the network')
            return
        self.vertexes.append(v)
        self.__addColumnRow()
        
    def addArch(self, s, e, w = 1):
        if self.__locate(s) == -1:
            self.addVertex(s)
        if self.__locate(e) == -1:
            self.addVertex(e)
        ps = self.__locate(s)
        pe = self.__locate(e)
        if self.mark in ['ug','dg']:
            w = 1
        self.adjMat[ps][pe] = w
        if self.mark in ['ug', 'un']:
            self.adjMat[pe][ps] = w
    
    def deleteArch(self, s, e):
        ps = self.__locate(s)
        pe = self.__locate(e)
        if ps == -1 or pe == -1:
            print('ERROR: arch not in the network!')
            return
        if self.adjMat[ps][pe] == self.__INFINITY:
            print('ERROR: arch not in the network')
            return
        self.adjMat[ps][pe] = self.__INFINITY
        if self.mark in ['ug','un']:
            self.adjMat[pe][ps] = self.__INFINITY
   
    def deleteVertex(self, v):
        pos = self.__locate(v)
        if pos == -1:
            print('ERROR: vertex not in the network!')
            return
        del self.vertexes [pos]
        del self.adjMat [pos]
        for i in range(len(self.adjMat)):
            del self.adjMat[i] [pos]
        
    def simplePath(self, s, e):
        if self.__locate(s) == -1 or self.__locate(e) == -1:
            print('ERROR: vertex not found!')
            return
        if s == e:
            print(s)
            return
        prior = []
        for i in range(len(self.vertexes)):
            prior += [-1]
        def path(self, s, e):
            if s == e:
                return True
            tmp = self.firstAdj(s)
            while tmp != -1:
                if prior[self.__locate(tmp)] == -1:
                    prior[self.__locate(tmp)] = self.__locate(s)
                    if tmp == e:
                        return True
                    if path(self, tmp, e):
                        return True
                else:    
                    #print('no path from', tmp)
                    tmp = self.nextAdj(tmp, s)
                    #print('changed to', tmp)
            return False
        def showPath(self, s, e):
            st = Stack()
            tmp = self.__locate(e)
            while prior[tmp] != self.__locate(s):
                st.push(tmp)
                tmp = prior[tmp]
            st.push(tmp)
            print(s, end = '')
            while st.top != 0:
                print('->', self.vertexes[st.pop()], end = '')
        if path(self, s, e):
            showPath(self, s, e)
        else:
            print('path does not exist')