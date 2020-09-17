# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:53:41 2020

@author: 86156
"""

class linkedList():
    '''
    linked list:
    attributes: 
        node:
            next pointer
            prior pointer
            value
        list:
            head pointer
            rear pointer
    methods: 
        insert a node into a certain position of a linked list
        delete a node from a linked list
        get a node from a linked list
        find the position of a node from a linked list
        update the value in a node of a linked list
    '''
    class node():
        def __init__(self, nextP = -1, priorP = -1, value = -1, address = -1):
            self.nextP = nextP
            self.priorP = priorP
            self.value = value
            self.address = address
            
    def __init__(self, nodes = [], rear = -1, head = -1, length = 0):
        self.nodes = nodes
        self.rear = rear
        self.head = head
        self.length = length
        
    def get(self, pos):
        if pos >= self.length or pos < 0:
            print("index out of range!")
            return
        n = self.nodes[self.head]
        i= 0
        while n.nextP != -1:
            if i == pos:
                return n
            n = self.nodes[n.nextP]
            i += 1
            
    def find(self, value):
        i = 0
        pos = self.head
        while pos != -1:
            if self.nodes[pos].value == value:
                return i
            i += 1
            pos = self.nodes[pos].nextP
        print("node not found!")
        
    def insert(self, pos, value):
        if pos < 0 or pos > self.length:
            print("ERROR: index error")
            return
        if value == -1:
            print("value can not be -1")
            return
        # check if there is position for newNode in nodes[]
        # if there is position in nodes[] use it firstly, if not make a new position
        flag = 0
        for i in range(len(self.nodes)):
            if self.nodes[i].value == -1:
                flag = 1
                newNode = self.nodes[i]
                newNode.address = i
                break
        if flag == 0:    
            newNode = self.node()
            newNode.address = len(self.nodes)
        newNode.value = value
        if self.length == 0:
            self.nodes += [newNode]
            self.head = 0
            self.rear = 0
            self.length += 1
            return
        if pos == 0:
            self.nodes[self.head].priorP = newNode.address
            newNode.nextP = self.head
            self.head = newNode.address
        elif pos == self.length:
            self.nodes[self.rear].nextP = newNode.address
            newNode.priorP = self.rear
            self.rear = newNode.address
        else:
            n = self.nodes[self.head]
            for i in range(pos):
                n = self.nodes[n.nextP]
            newNode.nextP = n.address
            newNode.priorP = n.priorP
            self.nodes[n.priorP].nextP = newNode.address
            n.priorP = newNode.address
        if flag == 0:
            self.nodes += [newNode]
        self.length += 1
        
    def delete(self, pos):
        if pos < 0 or pos >= self.length:
            print("ERROR: index out of range!")
            return
        n = self.head
        for i in range(pos):
            n = self.nodes[n].nextP
        if n != self.head:
            self.nodes[self.nodes[n].priorP].nextP = self.nodes[n].nextP
        else:
            self.head = self.nodes[n].nextP
        if n != self.rear:
            self.nodes[self.nodes[n].nextP].priorP = self.nodes[n].priorP
        else:
            self.rear = self.nodes[n].priorP
        self.nodes[n].value = -1
        self.length -= 1

    def update(self, pos, value):
        if pos < 0 or pos >= self.length:
            print("ERROR: index out of range!")
            return
        n = self.nodes[self.head]
        for i in range(pos):
            n = self.nodes[n.nextP]
        self.nodes[n.address].value = value
        
    def show(self):
        n = self.head
        while n != -1:
            print('->', self.nodes[n].value , end = '')
            n = self.nodes[n].nextP
        print(" ")
        
        
# test
if __name__ == '__main__':
    linkl = linkedList()
    for i in range(10):
        linkl.insert(i, 2*i)
        print(linkl.length, linkl.head, linkl.rear)
        linkl.show()
    linkl.insert(5, 5)
    print(linkl.length, linkl.head, linkl.rear)
    linkl.show()
    linkl.update(6, 6)
    linkl.show()
    linkl.delete(8)
    print(linkl.length, linkl.head, linkl.rear)    
    linkl.show()
        