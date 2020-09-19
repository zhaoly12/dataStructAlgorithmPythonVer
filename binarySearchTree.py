# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 08:22:30 2020

@author: 86156
"""

from binaryTree import binaryTree

class binarySearchTree(binaryTree):
    '''
    binarySearchTree:
    binary search tree is a special kind of binary tree
    data in nodes of a binary search tree should meet the condition:
        left child < parent < right child
    if you want to get a sorted list, traverse a binary search tree in l->d->r sequence
    because the sequence has to be kept, add, delete, Create will be rewritten
    other functions are all the same with binary tree
    '''
    
    def add(self, v):
        # if the tree is empty make a root node for it
        if self.nodes == [] or self.nodes[self.root] == -1:
            self.root = self.makeNode()
            self.nodes[self.root].value = v
            return
        pos = self.Find(v)
        # if the value is already in the tree
        if pos != -1:
            print('value already in the tree!')
            return
        pos = self.root
        flag = 0
        # add new value into the tree
        while True:
            if self.nodes[pos].value > v:
                if self.nodes[pos].lchild == -1:
                    break
                pos =self.nodes[pos].lchild
            else:
                if self.nodes[pos].rchild == -1:
                    flag = 1
                    break
                pos = self.nodes[pos].rchild
        address = self.makeNode()
        self.nodes[address].value = v
        self.nodes[address].parent = pos
        if flag == 0:
            self.nodes[pos].lchild = address
        else:
            self.nodes[pos].rchild = address
        
    def Create(self):
        v = int(input("please input an integer or a float, input -1 to terminate:"))
        while v != -1:
            self.add(v)
            self.Show()
            v = int(input("please input an integer or a float, input -1 to terminate:"))
        
    def delete(self, v):
        pos = self.Find(v)
        if pos == -1:
            print("value not in the tree")
            return
        vTmp = v
        # go from the value to be deleted
        # stop at a node which has no rchild
        # save all the positions in the route
        positions = []
        while self.nodes[pos].rchild != -1:
            positions.append(pos)
            pos = self.nextNode(vTmp, mode = 'm').address
            vTmp = self.nextNode(vTmp, mode = 'm').value  
        positions.append(pos)
        # copy data backward
        for i in range(len(positions)-1):
            self.nodes[positions[i]].value = self.nodes[positions[i+1]].value
        # delete the node
        if self.nodes[pos].lchild != -1:
            self.nodes[self.nodes[pos].lchild].parent = self.nodes[pos].parent
        if self.nodes[pos].parent != -1:
            if self.nodes[self.nodes[pos].parent].lchild == pos:
                self.nodes[self.nodes[pos].parent].lchild = self.nodes[pos].lchild
            else:
                self.nodes[self.nodes[pos].parent].rchild = self.nodes[pos].lchild
        else:
            self.root = self.nodes[pos].lchild
        # delete node from 'memory'
        self.nodes[pos] = -1
        if self.root == -1:
            self.nodes = []