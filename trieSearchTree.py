# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:05:18 2020

@author: 86156
"""

class trieSearchTree():
    '''
    trie search tree is a tree that allows user to get a value by input a certain word
    it is not a balanced tree and it is not a binary tree either
    '''

    class node():
        def __init__(self):
            self.keyValue = []
            self.parent = -1
            self.lchild = -1
            self.mchild = -1
            self.rchild = -1
            self.address = -1

    def __init__(self):
        self.nodes = [self.node()]
        self.root = 0
        self.nodes[0].keyValue = ['H']
    
    def malloc(self):
        n = self.node()
        n.address = len(self.nodes)
        self.nodes += [n]
        return n.address

    def destroy(self):
        self.root = -1
        self.nodes = []        
        
    # input a string and get a value
    def find(self, string):
        if isinstance(string, str) == False:
            print('please input a string to get value')
            return -1
        r = self.root
        i = string[0]
        count = 0
        while True:
            if r == -1:
                return -1
            if ord(i) < ord(self.nodes[r].keyValue[0]):
                r = self.nodes[r].lchild
            elif ord(i) > ord(self.nodes[r].keyValue[0]):
                r = self.nodes[r].rchild
            else:
                count += 1
                if count == len(string):
                    if len(self.nodes[r].keyValue) == 1:
                        return -1
                    else:
                        return r
                i = string[count]
                r = self.nodes[r].mchild
    
    def add(self, string, value):
        if isinstance(string, str) == False:
            print('please input a string as a key!')
            return
        if self.find(string) != -1:
            print('Update: old value:', self.nodes[self.find(string)].keyValue[1],\
                'new value:', value)
            self.nodes[self.find(string)].keyValue[1] = value
            return
        def handle(self, string, pos, value, length):
            if ord(string[length]) == ord(self.nodes[pos].keyValue[0]):
                if length == len(string)-1:
                    self.nodes[pos].keyValue += [value]
                    return
                if self.nodes[pos].mchild == -1:
                    self.nodes[pos].mchild = self.malloc()
                    self.nodes[self.nodes[pos].mchild].parent = pos
                    self.nodes[self.nodes[pos].mchild].keyValue = [string[length]]                
                handle(self, string, self.nodes[pos].mchild, value, length+1)
            elif ord(string[length]) < ord(self.nodes[pos].keyValue[0]):
                if self.nodes[pos].lchild == -1:
                    self.nodes[pos].lchild = self.malloc()
                    self.nodes[self.nodes[pos].lchild].parent = pos
                    self.nodes[self.nodes[pos].lchild].keyValue = [string[length]]
                if length == len(string) - 1:
                    self.nodes[self.nodes[pos].lchild].keyValue += [value]
                    return
                handle(self, string, self.nodes[pos].lchild, value, length)
            else:
                if self.nodes[pos].rchild == -1:
                    self.nodes[pos].rchild = self.malloc()
                    self.nodes[self.nodes[pos].rchild].parent = pos
                    self.nodes[self.nodes[pos].rchild].keyValue = [string[length]]
                if length == len(string) - 1:
                    self.nodes[self.nodes[pos].rchild].keyValue += [value]
                    return
                handle(self, string, self.nodes[pos].rchild, value, length)                                                
        handle(self, string, self.root, value, 0)
            
    