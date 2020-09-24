# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:50:30 2020

@author: 86156
"""

from binaryTree import binaryTree

class optimalBinarySearchTree(binaryTree):
    '''
    when using balanced tree, B+ tree or red black tree
    there is a hypothesis that all the keys have the same search frequence
    actually, they are different
    optimal binary search tree maybe an unbalanced tree but the expected searching cost is the least
    use dynamic programming to make a optimal binary search tree
    cautions:
        1. no matter what the root is, the sequence of traversing a optimal binary search tree in l->d->r mode is constant
        2. the sequence of key words in a optimal binary search tree is constant
        3. an optimal binary search tree offers the least searching cost not the highest possibility of hitting key words
    '''
    
    # using dynamic programming to create an optimal binary search tree
    def Create(self):
        i = 1
        pk = []
        pd = []
        d = float(input('please input the possibility of hitting the word before the first key word:'))
        pd.append(d)
        while True:
            k = float(input('please input the searching frequency of the key word, input -1 to end:'))
            if k == -1.0:
                break
            d = float(input('please input the possibility of hitting the word between this \
                            key word and the next key word:'))
            i += 1
            pk.append(k)
            pd.append(d)
        if sum(pk) + sum(pd) != 1:
            print('Warnning! total possibillity does not equal 1!')
        # the row of the dynamicMat stands for the start point of the sublist
        # the column of the dynamicMat stands for the end point of the sublist
        # dynamicMat[s][e] means the least cost of [dsksds+1......dekede+1]
        # root[s][e] is the position of root node
        dynamicMat = []
        root = []
        for i in range(len(pk)):
            dynamicMat.append([0])
            root.append([0])
        for i in range(len(pk)):
            count = 0
            while count < len(pk)-1:
                dynamicMat[i].append(0)
                root[i].append(0)
                count += 1
        # initialize
        for i in range(len(pk)):
            dynamicMat[i][i] = 2 * pd[i] + pk[i] + 2 * pd[i+1]
            root[i][i] = i
        ### main part
        # s is the start point of the sublist
        # n is the number of nodes in the tree
        # r is the root of the tree
        for n in range(2, len(pd)):
            for s in range(len(pk)-n+1):
                dynamicMat[s][n+s-1] = sum(pk[s:n+s]) + sum(pd[s:n+s+1]) + pd[s] + dynamicMat[s+1][n+s-1]
                root[s][n+s-1] = s
                for r in range(s+1, n+s-1):
                    if dynamicMat[s][n+s-1] > sum(pk[s:n+s]) + sum(pd[s:n+s+1]) + \
                                            dynamicMat[s][r-1] + dynamicMat[r+1][n+s-1]:
                        dynamicMat[s][n+s-1] = sum(pk[s:n+s]) + sum(pd[s:n+s+1]) + \
                                            dynamicMat[s][r-1] + dynamicMat[r+1][n+s-1]
                        root[s][n+s-1] = r
                if dynamicMat[s][n+s-1] > sum(pk[s:n+s]) + sum(pd[s:n+s+1]) + pd[n+s] + dynamicMat[s][n+s-2]:
                    dynamicMat[s][n+s-1] = sum(pk[s:n+s]) + sum(pd[s:n+s+1]) + pd[n+s] + dynamicMat[s][n+s-2]
                    root[s][n+s-1] = n+s-1
        print('the least searching cost is :', dynamicMat[0][len(pk)-1])
        ### store the data into binary tree
        def store(self, root, pk, pd):
            def handle(self, parent, newadd, start, end):
                if start > end:
                    return
                r = root[start][end]
                self.nodes[newadd].value = pk[r]
                self.nodes[newadd].parent = parent
                if start <= r-1:
                    self.nodes[newadd].lchild = self.makeNode()
                    handle(self, newadd, self.nodes[newadd].lchild, start, r-1)
                if start == r:
                    self.nodes[newadd].lchild = self.makeNode()
                    self.nodes[self.nodes[newadd].lchild].value = pd[r]
                    self.nodes[self.nodes[newadd].lchild].parent = newadd
                if r+1 <= end:
                    self.nodes[newadd].rchild = self.makeNode()
                    handle(self, newadd, self.nodes[newadd].rchild, r+1, end)
                if r == end:
                    self.nodes[newadd].rchild = self.makeNode()
                    self.nodes[self.nodes[newadd].rchild].value = pd[r+1]
                    self.nodes[self.nodes[newadd].rchild].parent = newadd                    
            self.root = self.makeNode()
            handle(self, -1, self.root, 0, len(pk)-1)
        store(self, root, pk, pd)
        
    def add(self, *params):
        print('add function disabled!')
        
    def delete(self, *params):
        print('delete function disabled!')        
    
    