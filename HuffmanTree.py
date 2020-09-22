# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:36:57 2020

@author: 86156
"""

from binaryTree import binaryTree

class HuffmanTree(binaryTree):
    '''
    Huffman tree is a tree with the least weighed path length
    use greedy algorithm to make a Huffman tree
    Huffman tree is a binary tree(it is a complete tree when created by greedy algorithm)
    '''            

    def Create(self):
        valueList = []
        while True:
            value = int(input('please input the weight, input -1 to end:'))
            if value == -1:
                break
            valueList.append(value)
        if len(valueList) < 2:
            print('ERROR: a Huffman tree should have at least two leaf nodes!')
            return
        valueList.sort()
        keyValue = []
        for i in range(len(valueList)):
            address = self.makeNode()
            self.nodes[address].value = valueList[i]
            keyValue += [(valueList[i], address)]
        while True:
            address = self.makeNode()
            self.nodes[address].value = keyValue[0][0] + keyValue[1][0]
            self.nodes[address].lchild = keyValue[0][1]
            self.nodes[address].rchild = keyValue[1][1]
            self.nodes[keyValue[0][1]].parent = address
            self.nodes[keyValue[1][1]].parent = address
            if len(keyValue) == 2:
                self.root = address
                self.Show()
                return
            keyValue += [(keyValue[0][0] + keyValue[1][0], address)]
            keyValue = keyValue[2:]
            keyValue.sort()
    
    def add(self, *params):
        print('disabled!')
        
    def delete(self, *params):
        print('disabled!')