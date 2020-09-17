# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:01:14 2020

@author: 86156
"""

class gList():
    '''
    generalized list:
        attribute:
            atom:
                value
            list:
                head pointer
                rear pointer
        methods:
            count the number of atoms
            get the length of a generalized list
            get the depth of a generalized list
            put a new element(atom or list into a generalized list)
    '''
    def __init__(self, gl = []):
        self.gl = gl
    
    def put(self, pos, data):
        if isinstance(self.gl, list) == False:
            l = [self.gl]
            self.gl = l
            print('atom changed to list!')
        if pos > len(self.gl) or pos < 0:
            print('ERROR: index error')
            return
        i = len(self.gl)
        self.gl += [0]
        while i > pos:
            self.gl[i] = self.gl[i-1]
            i -= 1
        self.gl[pos] = data
    
    def delete(self, pos):
        if isinstance(self.gl, list) == False:
            l = [self.gl]
            self.gl = l
            print('atom changed to list!')
        if pos >= len(self.gl) or pos < 0:
            print('ERROR: index error')
            return
        i = pos
        while i < len(self.gl)-1:
            self.gl[i] = self.gl[i+1]
            i += 1
        del self.gl[i]
        
    def update(self, pos, data):
        if isinstance(self.gl, list) == False:
            l = [self.gl]
            self.gl = l
            print('atom changed to list!')
        if pos >= len(self.gl) or pos < 0:
            print('ERROR: index error')
            return
        self.gl[pos] = data

    def atomNum(self, gl):
        if isinstance(gl, list) == False:
            return 1
        result = 0
        for i in gl:
            if isinstance(i, list):
                result += self.atomNum(i)
            else:
                result += 1
        return result

    @property                
    def length(self):
        if isinstance(self.gl, list):
            return len(self.gl)
        else:
            return 0
        
    def depth(self, gl):
        if isinstance(gl, list) == False:
            return 0
        else:
            result = 0
            for l in gl:
                if self.depth(l) > result:
                    result = self.depth(l)
            return result + 1
    
# test
if __name__ == "__main__":
    glist = gList(1)
    glist.update(0, 0)
    for i in range (1, 10):
        glist.put(i, 2*i)
        print(glist.gl)
        print('length is:', glist.length, 'depth is:', glist.depth(glist.gl), \
              'atom number is:', glist.atomNum(glist.gl))
    glist.put(5, [5,6])
    print(glist.gl)
    print('length is:', glist.length, 'depth is:', glist.depth(glist.gl), \
          'atom number is:', glist.atomNum(glist.gl))
    i = glist.length
    while i >= 1:
        glist.delete(i)
        print(glist.gl)
        print('length is:', glist.length, 'depth is:', glist.depth(glist.gl), \
              'atom number is:', glist.atomNum(glist.gl))
        i -= 1
        
        