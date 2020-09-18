# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:25:44 2020

@author: 86156
"""

from tree import tree

class forest(tree):
    '''
    see the first child as lchild
    see the sibling as rchild
    see the sibling of root as another tree
    then forest is can be seen as a special binary tree
    '''
    
    '''
    followings are the same with tree:
    def Show():
        the sibling of root stands for another tree
    def Depth():
        return the depth of the deepest tree in the forest
    '''
    
    '''
    followings are the same with binary tree:
    def Create():
        for a forest the forest is created in parent->children->sibling sequence
        the sibling of the root node is another tree
    def Traverse():
    def priorNode():
    def nextNode():
    def delete():
    def thread():
        for a forest mode = 'l'(d->l->r) means traverse in parent->children->siblings sequence
        mode = 'm'(l->d->r) means traverse in children->parent->siblings sequence
        mode = 'r'(l->r->d) means traverse in children->siblings->parent sequence(almost meaningless)
    def add():
        for a forest mode = 'l' means add the node as the first child of a node
        mode = 'r' means add the node as the sibling of a node
    '''
    
    # add a new Tree in the forest
    def addTree(self):
        prior = self.root
        while self.nodes[prior].rchild != -1:
            prior = self.nodes[prior].rchild
        # almost the same with creating a binary tree
        # the only difference is to find the prior root node and build the connection
        def createTree(self, prior):
            newRoot = self.makeNode()
            self.nodes[prior].rchild = newRoot
            print('create a tree, input the nodes in parent->children->sibling \
                  sequence input . to stands for null')
            def create(self, pos, p):
                    v = input("please input a character(. stands for a null node):")
                    if v == '.':
                        self.nodes[pos] = -1
                        if self.nodes[p].lchild == pos:
                            self.nodes[p].lchild = -1
                        else:
                            self.nodes[p].rchild = -1
                        return
                    self.nodes[pos].value = v
                    self.nodes[pos].parent = p
                    self.nodes[pos].address = pos
                    self.nodes[pos].lchild = self.makeNode()
                    create(self, self.nodes[pos].lchild, pos)
                    self.nodes[pos].rchild = self.makeNode()
                    create(self, self.nodes[pos].rchild, pos)
            create(self, newRoot, prior)
        createTree(self, prior)