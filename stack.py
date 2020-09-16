# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:44:47 2020

@author: 86156
"""

from seqList import seqList
from linkedList import linkedList

class Stack(seqList):
    '''
    stack is a special kind of linear list
    we can only add element in a stack from the top and can only delete element from the top
    all the other methods in stack are the same with that in sequential list  
    '''
    def __init__(self, length = 0, stack = [], top = 0, size = 100):
        self.length = length
        self.stack = stack
        self.top = top
        self.size = size
        
    def insert(self, pos, value):
        print("insert function is disabled in stack, please use push")
    
    def delete(self, pos):
        print("delete function is disabled in stack, please use pop")
        
    def update(self, pos, value):
        print("update function is disabled in stack")
        
    def push(self, value):
        if self.top == self.size:
            print("ERROR:stack overflow!")
            return
        self.length += 1
        self.stack += [value]
        self.top += 1
    
    def pop(self):
        if self.top == 0:
            return
        value = self.stack[self.top-1]
        del self.stack[self.top - 1]
        self.top -= 1
        self.length -= 1
        return value
    
class linkedStack(linkedList, Stack):
    
    def __init__(self, length = 0, top = 0, size = 100, nodes = [], rear = -1, head = 0):
        Stack.__init__(self, length, nodes, top, size)
        linkedList.__init__(self, nodes, rear, head)
    
    def insert(self, pos, value):
        print("insert function is disabled in stack, please use push")
    
    def delete(self, pos):
        print("delete function is disabled in stack, please use pop")
        
    def update(self, pos, value):
        print("update function is disabled in stack")    
    
    def push(self, value):
        if self.top == self.size:
            print("ERROR: stack overflow!")
            return
        if self.length == 0:
            self.head = 0
        self.length += 1
        newNode = self.node()
        newNode.value = value
        newNode.priorP = self.top-1
        newNode.address = self.top
        if self.top != 0:
            self.nodes[self.top-1].nextP = self.top
        self.top += 1
        self.nodes += [newNode]
        
    def pop(self):
        if self.top == 0:
            return
        value = self.nodes[self.top-1].value
        del self.nodes[self.top-1]
        if self.top > 1:
            self.nodes[self.top-2].nextP = -1
        else:
            self.head = -1
        self.top -= 1
        self.length -= 1
        return value
    
# test
if __name__ == '__main__':
    stack = Stack()
    i = 1
    while i < 5:
        stack.push(2*i)
        print(stack.stack)
        i += 1
    while stack.top != 0:
        value = stack.pop()
        print(stack.stack)
    
    lstack = linkedStack()
    i = 0
    while i < 5:
        lstack.push(2*i)
        lstack.show()
        i += 1
    while lstack.top != 0:
        value = lstack.pop()
        lstack.show()
        