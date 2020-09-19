# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 08:24:07 2020

@author: 86156
"""

from binarySearchTree import binarySearchTree

class redBlackTree(binarySearchTree):
    '''
    the red black tree is a special complete binary search tree
    for a red black tree the left child can be a red child 
    a red child is in the same depth with its parent(a red child is actually a sibling)
    all the leaf nodes in a red black tree has the same depth
    to keep the leaf nodes in the same depth, the root may be changed
    because of red child, function Depth and Show will be rewitten
    also for a red black tree a leaf node means a NULL node so function LeafNum will be rewritten
    because we have to keep the tree balanced, function add and delete will be rewritten
    other functions are the same with those in class binarySearchTree()
    '''
    
    @property
    def Depth(self):
        pos = self.root
        d = 0
        while pos != -1:
            d += 1
            pos = self.nodes[pos].rchild
        return d
            
    @property
    def LeafNum(self):
        def leafNum(self, root):
            if root == -1:
                return 0
            elif self.nodes[root].rchild == -1:
                if self.nodes[root].lchild == -1:
                    return 2
                else:
                    return 3
            else:
                return leafNum(self, self.nodes[root].rchild) + leafNum(self, self.nodes[root].lchild)    
        if self.nodes == []:
            return 0
        else:
            return leafNum(self, self.root)
        
    def Show(self):
        def show(self, root, layer):
            if root == -1 or self.nodes[root] == -1:
                print('')
                return
            if self.nodes[root].lchild != -1:
                if self.nodes[self.nodes[root].lchild].mark == 'r':
                    show(self, self.nodes[root].lchild, layer)
                else:
                    show(self, self.nodes[root].lchild, layer+1)
            else:
                print('')
            for i in range(layer):
                print('   ', end = '')
            print(self.nodes[root].value)
            show(self, self.nodes[root].rchild, layer+1)
        if self.nodes == []:
            return
        else:
            show(self, self.root, 1)
            
    def add(self, v):        
        pos = self.Find(v)
        if pos != -1:
            print('data already in the tree')
            return
        newadd = self.makeNode()
        self.nodes[newadd].value = v
        self.nodes[newadd].mark = 'r'
        pos = self.root
        # if the tree is an empty tree create a root for it
        if pos == -1:
            self.root = newadd
            self.nodes[newadd].mark = 'b'
            return
        # find the position and add the new value as a new leaf node            
        while True:
            if v < self.nodes[pos].value:
                if self.nodes[pos].lchild == -1:
                    self.nodes[pos].lchild = newadd
                    break
                pos = self.nodes[pos].lchild
            else:
                if self.nodes[pos].rchild == -1:
                    self.nodes[pos].rchild = newadd
                    break
                pos = self.nodes[pos].rchild
        self.nodes[newadd].parent = pos
        # check and do some adjustment
        while True:
            if self.nodes[pos].mark != 'r':# red(new) <- black ->?
                if self.nodes[pos].lchild == newadd:
                    return
                if self.nodes[pos].lchild == -1: # black -> red(new)
                    self.nodes[pos].mark = 'r'
                    self.nodes[newadd].mark = 'b'
                    self.nodes[pos].rchild = self.nodes[newadd].lchild
                    if self.nodes[pos].rchild != -1:
                        self.nodes[self.nodes[pos].rchild].parent = pos
                    self.nodes[newadd].lchild = pos
                    self.nodes[newadd].parent = self.nodes[pos].parent
                    self.nodes[pos].parent = newadd 
                    if self.nodes[newadd].parent == -1:
                        self.root = newadd
                        return
                    if self.nodes[self.nodes[newadd].parent].lchild == pos:
                        self.nodes[self.nodes[newadd].parent].lchild = newadd
                    else:
                        self.nodes[self.nodes[newadd].parent].rchild = newadd
                    return
                if self.nodes[self.nodes[pos].lchild].mark != 'r':# black <- black -> red(new)
                    self.nodes[pos].mark = 'r'
                    self.nodes[newadd].mark = 'b'
                    self.nodes[pos].rchild = self.nodes[newadd].lchild
                    if self.nodes[pos].rchild != -1:
                        self.nodes[self.nodes[pos].rchild].parent = pos
                    self.nodes[newadd].lchild = pos
                    self.nodes[newadd].parent = self.nodes[pos].parent
                    self.nodes[pos].parent = newadd 
                    if self.nodes[newadd].parent == -1:
                        self.root = newadd
                        return
                    if self.nodes[self.nodes[newadd].parent].lchild == pos:
                        self.nodes[self.nodes[newadd].parent].lchild = newadd
                    else:
                        self.nodes[self.nodes[newadd].parent].rchild = newadd
                    return                    
                else:# red <- black -> red(new)
                    self.nodes[self.nodes[pos].lchild].mark = 'b'
                    self.nodes[newadd].mark = 'b'
                    if self.nodes[pos].parent == -1:
                        return
                    self.nodes[pos].mark = 'r'
                    newadd = pos
                    pos = self.nodes[pos].parent
            else:
                if self.nodes[pos].lchild == newadd:# red(new) <- red<- black ->?
                    self.nodes[newadd].mark = 'b'
                    p = self.nodes[pos].parent
                    gp = self.nodes[self.nodes[pos].parent].parent
                    self.nodes[p].lchild = self.nodes[pos].rchild
                    if self.nodes[p].lchild != -1:
                        self.nodes[self.nodes[p].lchild].parent = p
                    self.nodes[pos].rchild = p
                    self.nodes[p].parent = pos
                    self.nodes[pos].parent = gp
                    if gp == -1:
                        self.nodes[pos].mark = 'b'
                        self.root = pos
                        return
                    if self.nodes[gp].lchild == p:
                        self.nodes[gp].lchild = pos
                    else:
                        self.nodes[gp].rchild = pos
                    newadd = pos
                    pos = gp
                else:# (red->red(new))<-black ->?
                    self.nodes[pos].rchild = self.nodes[newadd].lchild
                    self.nodes[self.nodes[pos].rchild].parent = pos
                    self.nodes[newadd].lchild = pos
                    self.nodes[newadd].parent = self.nodes[pos].parent
                    if self.nodes[self.nodes[pos].parent].lchild == pos:
                        self.nodes[self.nodes[pos].parent].lchild = newadd
                    else:
                        self.nodes[self.nodes[pos].parent].rchild = newadd
                    self.nodes[pos].parent = newadd
                    tmp = pos
                    pos = newadd
                    newadd = tmp
                    
    def repush(self, v):
        nodes = self.nodes
        self.nodes = []
        self.root = -1
        for n in nodes:
            if n != -1 and n.value != v:
                self.add(n.value)

    def delete(self, v):
        pos = self.Find(v)
        if pos == -1:
            print("value not in the tree")
            return
        vTmp = v
        # go from the value to be deleted
        # stop at a node which has no rchild and has a lchild
        # save all the positions in the route
        positions = []
        flag = 1
        while self.nodes[pos].rchild != -1 or self.nodes[pos].lchild == -1:
            positions.append(pos)
            if self.nextNode(vTmp, mode = 'm') == -1:
                flag = 0
                break
            pos = self.nextNode(vTmp, mode = 'm').address
            vTmp = self.nextNode(vTmp, mode = 'm').value  
        # if there is a node like that, just copy data backward and delete the red left node
        if flag == 1:
            positions.append(pos)
            # copy data backward
            for i in range(len(positions)-1):
                self.nodes[positions[i]].value = self.nodes[positions[i+1]].value
            self.nodes[self.nodes[pos].lchild].parent = self.nodes[pos].parent
            self.nodes[self.nodes[pos].lchild].mark = 'b'
            if self.nodes[pos].parent != -1:
                if self.nodes[self.nodes[pos].parent].lchild == pos:
                    self.nodes[self.nodes[pos].parent].lchild = self.nodes[pos].lchild
                else:
                    self.nodes[self.nodes[pos].parent].rchild = self.nodes[pos].lchild
            else:
                self.root = self.nodes[pos].lchild
            # delete node from 'memory'
            self.nodes[pos] = -1
        # if there is no node like that repush all nodes except v
        else:
            self.repush(v)
        