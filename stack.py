# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:44:47 2020

@author: 86156
"""
from . import seqList

class stack(seqList):
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
        value = self.stack[self.top-1]
        del self.stack[self.top - 1]
        self.top -= 1
        self.length -= 1
        return value
    
class linkedStack():
    pass
    
# test
if __name__ == '__main__':
    stack = stack()
    i = 1
    while i < 5:
        stack.push(2*i)
        i += 1
    value = stack.pop()
        