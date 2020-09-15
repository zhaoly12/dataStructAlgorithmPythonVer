# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:41:34 2020

@author: 86156
"""

from . import seqList

class queue(seqList):
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
        del self.queue[0]
        self.front += 1
        self.length -= 1
        return value
    
    def empty(self):
        if self.rear == self.front:
            print("empty queue")
        else:
            print("this queue is not empty")
        
    def update(self, pos, value):
        print("update function is disabled in queue")


class circularQueue(queue):
    '''
    circular queue is a special kind of queue which has a decided length
    its rear pointer and front pointer move in cricle
    '''
    def __init__(self, length = 0, queue = [], front = 0, rear = 0, size = 10):
        super().__init__(length, queue, front, rear)
        self.size = size
    
    def insert(self, value):
        if self.rear - self.front == self.size:
            print("ERROR: full queue")
            return
        self.length += 1
        self.rear = (self.rear + 1)%(self.size + 1)
        self.queue += [value]
        
    def delete(self):
        value = self.queue[0]
        del self.queue[0]
        self.length -= 1
        self.front = (self.front + 1)%(self.size + 1)
        return value

class linkedQueue():
    pass

# test
if  __name__ == '__main__':
    q = queue()
    q.empty()
    for i in range(10):
        q.insert(2*i)
        print('queue:', q.queue, 'rear:', q.rear, 'front:', q.front)
    for i in range(10):
        q.delete()
        print('queue:', q.queue, 'rear:', q.rear, 'front:', q.front)
    q.empty()
    
    cirQue = circularQueue()
    cirQue.empty()
    for i in range(11):
        cirQue.insert(2*i)
        print('queue:', cirQue.queue, 'rear:', cirQue.rear, 'front:', cirQue.front)
    for i in range(10):
        cirQue.delete()
        print('queue:', cirQue.queue, 'rear:', cirQue.rear, 'front:', cirQue.front)
    cirQue.empty()
    


        
        