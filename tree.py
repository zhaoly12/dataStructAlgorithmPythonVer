# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:02:05 2020

@author: 86156
"""

from binaryTree import binaryTree

class tree(binaryTree):
    '''
    see the firstchild as the left child
    see the nextsibling as the right child
    then a tree can be seen as a special binary tree(the root only has left child)
    be careful that for a tree parent may be not the real parent when the node is a sibling of another node
    '''
        
    @property
    def Depth(self):
        def depth(self, root):
            if root == -1:
                return 0
            # here is a little difference
            # for a tree the rchild stands for sibling
            if depth(self, self.nodes[root].lchild) > depth(self, self.nodes[root].rchild)-1:
                d = depth(self, self.nodes[root].lchild)
            else:
                d = depth(self, self.nodes[root].rchild) - 1
            return d + 1
        if self.nodes == []:
            return 0
        else:
            return depth(self, self.root)
        
    @property
    def LeafNum(self):
        def leafNum(self, root):
            if root == -1:
                return 0
            # here is a difference is a node has no lchild(first child) the node is a leaf
            # then we should check its rchild(sibling)
            if self.nodes[root].lchild == -1:
                return 1 + leafNum(self, self.nodes[root].rchild)
            return leafNum(self, self.nodes[root].lchild) + leafNum(self, self.nodes[root].rchild)
        if self.nodes == []:
            return 0
        else:
            return leafNum(self, self.root)
        
    def Show(self):
        def show(self, root, layer):
            if root == -1 or self.nodes[root] == -1:
                print('')
                return
            show(self, self.nodes[root].lchild, layer+1)
            for i in range(layer):
                print("   ", end = '')
            print(self.nodes[root].value)
            # here is a little difference
            # for a tree the rchild stands for sibling
            show(self, self.nodes[root].rchild, layer)
        if self.nodes == []:
            return
        else:
            show(self, self.root, 1)
    
    '''
    followings are the same with binary tree:
    def Create():
        for a tree the tree is created in parent->children->sibling sequence
        keep in mind that the root node has no sibling
    def Traverse():
    def priorNode():
    def nextNode():
    def delete():
    def thread():
        for a tree mode = 'l'(d->l->r) means traverse in parent->children->siblings sequence
        mode = 'm'(l->d->r) means traverse in children->parent->siblings sequence
        mode = 'r'(l->r->d) means traverse in children->siblings->parent sequence(almost meaningless)
    def add():
        for a tree mode = 'l' means add the node as the first child of a node
        mode = 'r' means add the node as the sibling of a node
    '''