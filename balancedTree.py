# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:45:59 2020

@author: 86156
"""

class balancedTree():
    '''
    balanced tree:
        attribute:
            depth
            number of leaf nodes
            degree of a balanced tree
        method:
            count the depth of a balanced tree
            count the leaf nodes of a balanced tree
            show a balanced tree
            traverse a balanced tree
            get value from a balanced tree using a key
            find the prior node of a node
            find the next node of a node
            add key => value into a balanced tree
            delete key => value from a balanced tree
            update key => value of a balanced tree
            create a balanced tree
            destroy a balanced tree
    '''
    
    def __init__(self):
        self.degree = 3
        self.root = -1
        self.nodes = []
        
    class node():
        def __init__(self):
            self.keyValue = []
            self.children= []
            self.parent = -1
            self.address = -1
            self.num = 0 # number of child nodes
        
    def malloc(self):
        n = self.node()
        for i in range(len(self.nodes)):
            if self.nodes[i] == -1:
                n.address = i
                self.nodes[i] = n
                return i
        n.address = len(self.nodes)
        self.nodes += [n]     
        return n.address
    
    def free(self, address):
        try:
            self.nodes[address] = -1
            if len(self.nodes == 1):
                self.nodes = []
                self.root = -1
        except:
            print("ERROR: index error")
    
    @property
    def Depth(self):
        def depth(self, root):
            if root == -1:
                return 0
            if self.nodes[root].children == []:
                return 1
            d = 0
            for i in self.nodes[root].children:
                if depth(self, i) > d:
                    d = depth(self, i)
            return d + 1
        return depth(self, self.root)
    
    @property
    def LeafNum(self):
        def leafNum(self, root):
            if root == -1:
                return 0
            if self.nodes[root].children == []:
                return 1
            num = 0
            for i in self.nodes[root].children:
                num = num + leafNum(self, i)
            return num
        return leafNum(self, self.root)
    
    def Show(self):
        def show(self, root, layer):
            if root == -1:
                return
            for i in range(int(self.nodes[root].num/2)):
                show(self, self.nodes[root].children[i], layer + 3)
            for i in range(layer):
                print('   ', end = '')
            for kv in self.nodes[root].keyValue:
                print(kv[0], '=>', kv[1], ',',end = '')
            print('')
            for i in range(int(self.nodes[root].num/2), self.nodes[root].num):
                show(self, self.nodes[root].children[i], layer + 3)
        show(self, self.root, 1)
        
    def Traverse(self):
        def traverse(self, root):
            if root == -1:
                return
            if self.nodes[root].num > 0:
                for i in range(self.nodes[root].num - 1):
                    traverse(self, self.nodes[root].children[i])
                    print(self.nodes[root].keyValue[i][0], '=>', \
                          self.nodes[root].keyValue[i][1], ',', end = '')
                traverse(self, self.nodes[root].children[self.nodes[root].num - 1])
            else:
                for kv in self.nodes[root].keyValue:
                    print(kv[0], '=>', kv[1], ',', end = '')
        traverse(self, self.root)
        
    def Find(self, key):
        def find(self, root, key):
            if root == -1:
                return -1
            if self.nodes[root].num == 0:
                i = 0
                for k,v in self.nodes[root].keyValue:
                    if k == key:
                        return (root, i)
                    i += 1
                return -1
            for i in range(len(self.nodes[root].keyValue)):
                if key < self.nodes[root].keyValue[i][0]:
                    return find(self, self.nodes[root].children[i], key)
                if key == self.nodes[root].keyValue[i][0]:
                    return (root, i)
            return find(self, self.nodes[root].children[self.nodes[root].num - 1], key)
        return find(self, self.root, key)
    
    # add new key=>value into a balanced tree
    def add(self, key , value):
        # if the key has already been in the tree update the value
        if self.Find(key) != -1:
            pos = self.Find(key)[0]
            index = self.Find(key)[1]
            print('[Update]: key = ', key, \
                  'old value = ', self.nodes[pos].keyValue[index][1], 'new value = ', value)
            self.nodes[pos].keyValue[index] = (key, value)
            return
        # if the tree is empty make a root for it
        if self.root == -1:
            self.root = self.malloc()
            self.nodes[self.root].keyValue = [(key, value)]
            return
        # find the leaf node to add data
        pos = self.root
        index = 0
        while True:
            flag = 0
            for i in range(len(self.nodes[pos].keyValue)):
                if self.nodes[pos].keyValue[i][0] > key:
                    index = i
                    flag = 1
                    break
            if flag == 0:
                index = len(self.nodes[pos].keyValue)
            if self.nodes[pos].num == 0:
                break
            pos = self.nodes[pos].children[index]
        # add the key=>value
        kTmp = key
        vTmp = value
        while True:
            # add key => value no matter it is legal or not
            i = len(self.nodes[pos].keyValue)
            self.nodes[pos].keyValue += [0]
            while i > index:
                self.nodes[pos].keyValue[i] = self.nodes[pos].keyValue[i-1]
                i-= 1
            self.nodes[pos].keyValue[index] = (kTmp, vTmp)
            # check
            if len(self.nodes[pos].keyValue) < self.degree:# legal
                return
            # if illeagal go to the parent node and check 
            else:
                # split the node into two nodes and push the middle key, value upward
                (kTmp, vTmp) = self.nodes[pos].keyValue[int(len(self.nodes[pos].keyValue)/2)]
                newNode = self.malloc()
                # move key=>value from node into newNode 
                for i in range(int(len(self.nodes[pos].keyValue)/2) + 1, len(self.nodes[pos].keyValue)):
                    self.nodes[newNode].keyValue.append(self.nodes[pos].keyValue[i])
                # build the connection between newNode and child nodes
                if self.nodes[pos].num > 0:
                    for i in range(int(len(self.nodes[pos].keyValue)/2) + 1, self.nodes[pos].num):
                        self.nodes[newNode].children.append(self.nodes[pos].children[i])
                        self.nodes[self.nodes[pos].children[i]].parent = newNode
                    self.nodes[newNode].num = self.nodes[pos].num - 1 - \
                                                int(len(self.nodes[pos].keyValue)/2)
                    del self.nodes[pos].children [int(len(self.nodes[pos].keyValue)/2) + 1:]
                    self.nodes[pos].num = int(len(self.nodes[pos].keyValue)/2) + 1 
                del self.nodes[pos].keyValue [int(len(self.nodes[pos].keyValue)/2) : ]
                # build the connection between newNode and parent node
                if self.nodes[pos].parent != -1:
                    self.nodes[newNode].parent = self.nodes[pos].parent
                    rank = 0
                    while self.nodes[self.nodes[pos].parent].children[rank] != pos:
                        rank += 1
                    self.nodes[self.nodes[pos].parent].children += [0]
                    i = self.nodes[self.nodes[pos].parent].num
                    self.nodes[self.nodes[pos].parent].num += 1
                    while i > rank:
                        self.nodes[self.nodes[pos].parent].children[i] = \
                        self.nodes[self.nodes[pos].parent].children[i-1]
                        i -= 1
                    self.nodes[self.nodes[pos].parent].children[rank+1] = newNode
                    # next node to be checked is the parent node
                    pos = self.nodes[pos].parent
                    index = rank
                # if the node is root node make a new root
                else:
                    self.root = self.malloc()
                    self.nodes[self.root].keyValue = [(kTmp, vTmp)]
                    self.nodes[self.root].children = [pos, newNode]
                    self.nodes[self.root].num = 2
                    self.nodes[pos].parent = self.root
                    self.nodes[newNode].parent = self.root
                    return
        
    def Create(self):
        print('create a balanced tree:')
        self.degree = int(input('please input the degree(>=3) of the balanced tree:'))
        while self.degree < 3:
            self.degree = int(input('please input the degree again(degree >= 3)!:'))
        while True:
            key = int(input("please input a key, input -1 to terminate:"))
            if key == -1:
                break
            value = int(input('please input a value:'))
            self.add(key, value)
            self.Show()

    def destory(self):
        self.nodes = []
        self.root = -1
        self.degree = 3

    def priorkV(self, key):
        if self.Find(key) == -1:
            return -1
        (pos, index) = self.Find(key)
        # if the node has a child node 
        # the prior node is the rightmost node of its child tree [index]
        flag = 0
        while self.nodes[pos].num > 0:
            flag = 1
            pos = self.nodes[pos].children[index]
            index = self.nodes[pos].num - 1
        if flag == 1:
            index = len(self.nodes[pos].keyValue) - 1
            return (pos, index)
        # the node is a leaf node
        while True:
            # the index is not the first one
            # return the prior index
            if index != 0:
                index = index - 1
                return (pos, index)
            # go to its parent node and check
            if self.nodes[pos].parent == -1:
                return -1
            index = 0
            while self.nodes[self.nodes[pos].parent].children[index] != pos:
                index += 1
            pos = self.nodes[pos].parent
        return -1                

    def nextkV(self, key):
        if self.Find(key) == -1:
            return -1
        (pos, index) = self.Find(key)
        # the next node is the leftmost node of its child tree [index+1]
        flag = 0
        while self.nodes[pos].num > 0:
            flag = 1
            pos = self.nodes[pos].children[index + 1]
            index = -1
        if flag == 1:
            return (pos, 0)
        # the node is a leaf node
        while True:
            # the index is not the last index
            if index < len(self.nodes[pos].keyValue) - 1:
                index += 1
                return (pos, index)
            # go to the parent node and check
            index = 0
            if self.nodes[pos].parent == -1:
                return -1
            while self.nodes[self.nodes[pos].parent].children[index] != pos:
                index += 1
            pos = self.nodes[pos].parent
            index -= 1
        return -1

    def repush(self, key):
        ns = self.nodes
        self.nodes = []
        self.root = -1
        for n in ns:
            for k, v in n.keyValue:
                if k != key:
                    self.add(k, v)
        
    def delete(self, key):
        if self.Find(key) == -1:
            print("ERROR: key not found in the tree!")
            return
        (pos, index) = self.Find(key)        
        # if the key is already the last key of the tree, clear the tree
        if len(self.nodes) == 1 and len(self.nodes[pos].keyValue) == 1:
            self.destory()
            return
        # go from the target key and stop at a leaf node that has more than one key
        nextNodes = []
        priorNodes = []
        flag = 0
        nextPos = priorPos = pos
        nextIndex = priorIndex = index
        nextKey = priorKey = key
        while self.nextkV(nextKey) != -1 or self.priorkV(priorKey) != -1:
            if self.nextkV(nextKey) != -1:
                nextNodes.append((nextPos, nextIndex))
                if self.nodes[nextPos].num == 0 and len(self.nodes[nextPos].keyValue) > 1:
                    flag = 1
                    break
                (nextPos, nextIndex) = self.nextkV(nextKey)
                nextKey = self.nodes[nextPos].keyValue[nextIndex][0]
            if self.priorkV(priorKey) != -1:
                priorNodes.append((priorPos, priorIndex))
                if self.nodes[priorPos].num == 0 and len(self.nodes[priorPos].keyValue) > 1:
                    flag = -1
                    break
                (priorPos, priorIndex) = self.priorkV(priorKey)
                priorKey = self.nodes[priorPos].keyValue[priorIndex][0]
        # if all leaf nodes has only one key, repush
        #########################
        print('flag == ',flag)
        #######################
        if flag == 0:
            self.repush(key)
            return
        # move and delete 
        if flag == 1:
            for i in range(len(nextNodes)-1):
                self.nodes[nextNodes[i][0]].keyValue[nextNodes[i][1]] = \
                self.nodes[nextNodes[i+1][0]].keyValue[nextNodes[i+1][1]]
            del self.nodes[nextNodes[-1][0]].keyValue [nextNodes[-1][1]]
        else:
            for i in range(len(priorNodes)-1):
                self.nodes[priorNodes[i][0]].keyValue[priorNodes[i][1]] = \
                self.nodes[priorNodes[i+1][0]].keyValue[priorNodes[i+1][1]]
            del self.nodes[priorNodes[-1][0]].keyValue [priorNodes[-1][1]]
            