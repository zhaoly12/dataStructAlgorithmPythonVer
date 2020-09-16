# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:31:51 2020

@author: 86156
"""

class seqList(object):
    '''
    sequential list:
    attributes:
        index of an element
        value of an element
        length of a sequence list
    methods:
        find the position of an element in a sequence
        get an element from a sequence list
        insert an element into a certain place
        delete an element from a sequence list
        update an element of a sequence
    '''
    
    def __init__(self, length = 0, seql = []):
        self.length = length
        self.seql = seql
    
    def get(self, pos):
        if pos >= self.length or pos < 0:
            print("index out of range!")
        else:
            return self.seql[pos]
    
    def find(self, value):
        i = 0
        while i < self.length:
            if self.seql[i] == value:
                return i
            else:
                i += 1
        print(value, "not found")
    
    def insert(self, pos, value):    
        if pos > self.length or pos < 0:
            print("index out of range!")
        else:
            self.seql += [1]
            i = self.length
            while i >= pos:
                self.seql[i] = self.seql[i-1]
                i -= 1
            self.seql[pos] = value
            self.length += 1
    
    def delete(self, pos):
        if pos < 0 or pos >= self.length:
            print("index out of range!")
        else:
            i = pos
            while i < self.length-1:
                self.seql[i] = self.seql[i+1]
                i += 1
            del self.seql[self.length-1]
            self.length -= 1
        
    def update(self, pos, value):
        if pos < 0 or pos >=self.length:
            print("index out of range!")
        else:
            self.seql[pos] = value
        
# test
if __name__ == '__main__':
    seql = seqList()
    i = 0
    while i < 10:
        seql.insert(i, 2*i)
        i += 1
    seql.find(6)
    seql.find(100)
    seql.get(10)
    seql.get(5)
    seql.update(3, 3)
    seql.delete(4)
        
        
        