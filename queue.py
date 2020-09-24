# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:41:34 2020

@author: 86156
"""

from seqList import seqList
from linkedList import linkedList

class Queue(seqList):
    '''
    queue is a special kind of linear list
    for a queue value can only be added from the end of the list and deleted from the other end
    all the other methods are the same
    '''
    def __init__(self, length = 0, queue = [], front = 0, rear = 0):
        self.length = length
        self.queue = queue
        self.front = front
        self.rear = rear
        
    def insert(self, value):
        self.queue += [value]
        self.rear += 1
        self.length += 1
    
    def delete(self):
        value = self.queue[0]
        del self.queue[0] ## also here can be self.queue[0] = -1 (soft delete)
        self.front += 1
        self.length -= 1
        return value
    
    def empty(self):
        if self.rear == self.front:
            #print("empty queue")
            return True
        else:
            #print("this queue is not empty")
            return False
        
    def update(self, pos, value):
        print("update function is disabled in queue")


class circularQueue(Queue):
    '''
    circular queue is a special kind of queue which has a decided length
    its rear pointer and front pointer move in cricle
    '''
    def __init__(self, length = 0, nodes = [], front = 0, rear = 0, size = 10):
        super().__init__(length, nodes, front, rear)
        self.size = size
    
    def insert(self, value):
        if self.front == (self.rear + 1)%self.size:
            print("ERROR: full queue")
            return
        self.length += 1
        self.rear = (self.rear + 1)%(self.size)
        self.queue += [value]
        
    def delete(self):
        if(self.front == self.rear):
            print("already empty!")
            return
        value = self.queue[0]
        del self.queue[0] ## also here can be self.queue[0] == -1 (soft delete)
        self.length -= 1
        self.front = (self.front + 1)%(self.size)
        return value

class linkedQueue(linkedList, Queue):
    
    def __init__(self, nodes = [], rear = -1, head = -1, length = 0, front = -1):
        super().__init__(nodes, rear, head, length)
        self.front = front
        
    def insert(self, value):
        newNode = self.node()
        newNode.value = value
        if len(self.nodes) == 0:
            newNode.address = 0
            self.nodes += [newNode]
            self.rear = 0
            self.head = 0
            self.front = 0
            self.length = 1
            return
        flag = 0
        if len(self.nodes) > self.length:
            for i in range(len(self.nodes)):
                if self.nodes[i].value == -1:
                    newNode.address = i
                    break
        else:
            flag = 1
            newNode.address = self.length
        for i in range(len(self.nodes)):
            if self.nodes[i].nextP == -1:
                newNode.priorP = i
                self.nodes[i].nextP = newNode.address
                break
        if flag == 1:
            self.nodes += [newNode]
        else:
            self.nodes[newNode.address] = newNode
        self.rear = newNode.address
        self.length += 1
        
    def delete(self):
        if(self.length == 0):
            print('queue is already empty!')
            return
        self.front = self.nodes[self.head].nextP
        self.nodes[self.nodes[self.head].nextP].priorP = -1
        self.nodes[self.head].value = -1
        self.head = self.front
        self.length -= 1
        if(self.length == 0):
            self.rear = -1
            self.nodes = []
        
    def update(self, pos, value):
        print('update function is disabled in queue')

    def empty(self):
        if self.front == -1:
            print('empty queue')
        else:
            print('the queue is not empty')

# test
if  __name__ == '__main__':
    q = Queue()
    q.empty()
    for i in range(10):
        q.insert(2*i)
        print('queue:', q.queue, 'rear:', q.rear, 'front:', q.front)
    for i in range(5):
        q.delete()
        print('queue:', q.queue, 'rear:', q.rear, 'front:', q.front)
    q.empty()
    for i in range(6):
        q.insert(2*i+1)
        print('queue:', q.queue, 'rear:', q.rear, 'front:', q.front)
    q.empty()
    
    cirQue = circularQueue()
    cirQue.empty()
    for i in range(10):
        cirQue.insert(2*i)
        print('queue:', cirQue.queue, 'rear:', cirQue.rear, 'front:', cirQue.front)
    for i in range(5):
        cirQue.delete()
        print('queue:', cirQue.queue, 'rear:', cirQue.rear, 'front:', cirQue.front)
    cirQue.empty()
    for i in range(6):
        cirQue.insert(2*i+1)
        print('queue:', cirQue.queue, 'rear:', cirQue.rear, 'front:', cirQue.front)
    cirQue.empty()
    
    linkQue = linkedQueue()
    linkQue.empty()
    for i in range(10):
        linkQue.insert(2*i)
        linkQue.show()
        print('rear:', linkQue.rear, 'front:', linkQue.front)
    for i in range(5):
        linkQue.delete()
        linkQue.show()
        print('rear:', linkQue.rear, 'front:', linkQue.front)
    linkQue.empty()
    for i in range(6):
        linkQue.insert(2*i+1)
        linkQue.show()
        print('rear:', linkQue.rear, 'front:', linkQue.front)
    linkQue.empty()

        
        