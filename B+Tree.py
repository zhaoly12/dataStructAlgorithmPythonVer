# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:17:20 2020

@author: 86156
"""

from balancedTree import balancedTree
from linkedList import linkedList

class BPlusTree(balancedTree):
    '''
    B+ tree
    the structures of balanced tree and B+ tree are very alike
    B+ tree use a linked list to link all the key=>value
    B+ tree only stores value in leaf nodes('value' in leaf nodes are pointers pointed at linked list)
    all keys can be found in leaf nodes but may be not found in inner nodes
    '''
    
    data = linkedList()
        
    def Show(self):
        def show(self, root, layer):
            if root == -1:
                return
            for i in range(int(self.nodes[root].num/2)):
                show(self, self.nodes[root].children[i], layer + 3)
            for i in range(layer):
                print('   ', end = '')
            if self.nodes[root].children == []:
                for kv in self.nodes[root].keyValue:
                    print(kv[0], '=>', self.data.get(kv[1]).value, ',',end = '')
            else:
                for kv in self.nodes[root].keyValue:
                    print(kv[0], ',',end = '')                
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
                    print(self.nodes[root].keyValue[i][0], ',', end = '')
                traverse(self, self.nodes[root].children[self.nodes[root].num - 1])
            else:
                for kv in self.nodes[root].keyValue:
                    print(kv[0], '=>', self.data.get(kv[1]).value, ',', end = '')
        traverse(self, self.root)
    
    # find the leaf node using key
    def Find(self, key):
        def find(self, root, key):
            if root == -1:
                return -1
            if self.nodes[root].num == 0:
                i = 0
                for kv in self.nodes[root].keyValue:
                    if kv[0] == key:
                        return (root, i)
                    i += 1
                return -1
            for i in range(len(self.nodes[root].keyValue)):
                if key <= self.nodes[root].keyValue[i][0]:
                    return find(self, self.nodes[root].children[i], key)
            return find(self, self.nodes[root].children[self.nodes[root].num - 1], key)
        return find(self, self.root, key)
    
    def add(self, key, value):
        # if the key has already been in the tree update the value
        if self.Find(key) != -1:
            pos = self.Find(key)[0]
            index = self.Find(key)[1]
            print('[Update]: key = ', key, \
                  'old value = ', self.data.get(self.nodes[pos].keyValue[index][1]).value,\
                  'new value = ', value)
            self.data.nodes[self.data.get(self.nodes[pos].keyValue[index][1]).address].value \
            = value
            return
        # add value into linked list and add its address into the leaf node in B+ tree
        self.data.insert(self.data.length, value)
        # the following variable value stands for the address of the real value in linked list
        value = self.data.length - 1
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
                if self.nodes[pos].keyValue[i][0] >= key:
                    index = i
                    flag = 1
                    break
            if flag == 0:
                index = len(self.nodes[pos].keyValue)
            if self.nodes[pos].num == 0:
                break
            pos = self.nodes[pos].children[index]
        # add the key=>value
        kvTmp = (key, value)
        while True:
            # add key => value no matter it is legal or not
            i = len(self.nodes[pos].keyValue)
            self.nodes[pos].keyValue += [0]
            while i > index:
                self.nodes[pos].keyValue[i] = self.nodes[pos].keyValue[i-1]
                i-= 1
            self.nodes[pos].keyValue[index] = kvTmp
            # check
            if len(self.nodes[pos].keyValue) < self.degree:# legal
                return
            # if illeagal go to the parent node and check 
            else:
                # split the node into two nodes and push the middle key upward
                # for a B+ tree, keys will be pushed upward values will be kept in leaf node! 
                kvTmp = (self.nodes[pos].keyValue[int(len(self.nodes[pos].keyValue)/2)][0],)
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
                ########## here is different from that in a balanced tree #######
                # for B+ tree key in a leaf node should be copied to its parent #
                if self.nodes[pos].num == 0:
                    del self.nodes[pos].keyValue [int(len(self.nodes[pos].keyValue)/2) + 1: ]
                else:
                    del self.nodes[pos].keyValue [int(len(self.nodes[pos].keyValue)/2): ]
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
                    self.nodes[self.root].keyValue = [kvTmp]
                    self.nodes[self.root].children = [pos, newNode]
                    self.nodes[self.root].num = 2
                    self.nodes[pos].parent = self.root
                    self.nodes[newNode].parent = self.root
                    return
        
    def priorkV(self, key):
        if self.Find(key) == -1:
            return -1
        (pos, index) = self.Find(key)
        # for a B+ tree the node must be a leaf node
        while True:
            # the index is not the first one
            # return the prior index
            if index != 0:
                index = index - 1
                return self.Find(self.nodes[pos].keyValue[index][0])
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
        # for a B+ tree the node must be a leaf node
        while True:
            # the index is not the last index
            if index < len(self.nodes[pos].keyValue) - 1:
                index += 1
                return self.Find(self.nodes[pos].keyValue[index][0])
            # go to the parent node and check
            index = 0
            if self.nodes[pos].parent == -1:
                return -1
            while self.nodes[self.nodes[pos].parent].children[index] != pos:
                index += 1
            pos = self.nodes[pos].parent
            index -= 1
        return -1       
        
    def destroy(self):
        self.root = -1
        self.nodes = []
        self.degree = 3
        self.data = linkedList()
        
    def repush(self, key):
        ns = self.nodes
        d = self.data
        self.nodes = []
        self.root = -1
        self.data = linkedList()
        self.data.nodes = []
        for n in ns:
            for kv in n.keyValue:
                if len(kv) > 1 and kv[0] != key:
                    self.add(kv[0], d.get(kv[1]).value)
        
    def delete(self, key):
        if self.Find(key) == -1:
            print("ERROR: key not found in the tree!")
            return
        self.repush(key)
        
    