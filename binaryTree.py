# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:04:13 2020

@author: 86156
"""

class binaryTree:
    '''
    binary tree:
        attribute:
            node
            parent node
            left child node
            right child node
            value
        method:
            traverse in left->node->right/left->right->node/node->left->right sequence
            show the tree
            count the depth of the tree
            count the number of leaf nodes in the tree
            add a node into the tree
            delete a node into the tree
            thread a tree
            find the position of a node using its value
            find the next node of a node when traverse in a certain sequence
            find the prior node of a node when traverse in a certain sequence
    '''
    
    def __init__(self):
        self.root = -1
        self.nodes = []
        
    class node():
        def __init__(self):
            self.value = -1
            self.parent = -1
            self.lchild = -1
            self.rchild = -1
            self.address = -1
            self.mark = -1
       
        @staticmethod
        def malloc(nodes):
            try:
                for i in nodes:
                    if i.value == -1:
                        return i
            except:
                return -1
            finally:
                return -1
        
        @staticmethod
        def free(nodes, pos):
            if pos < 0 or pos >= len(nodes):
                return
            nodes[pos] = -1
            if len(nodes) == 1:
                nodes = []
                
    def makeNode(self):
        index = self.node().malloc(self.nodes)
        if index == -1:
            index = len(self.nodes)
            self.nodes += [0]
        n = self.node()
        n.address = index
        self.nodes[index] = n
        return index
     
    @property
    def Depth(self):
        def depth(self, root):
            if root == -1:
                return 0
            if depth(self, self.nodes[root].lchild) > depth(self, self.nodes[root].rchild):
                d = depth(self, self.nodes[root].lchild)
            else:
                d = depth(self, self.nodes[root].rchild)
            return d + 1
        if self.nodes == []:
            return 0
        else:
            return depth(self, self.root)
    
    @property
    def LeafNum(self):
        def leafNum(self, root):
            if root == -1:
                return 0
            if self.nodes[root].rchild == -1 and self.nodes[root].lchild == -1:
                return 1
            return leafNum(self, self.nodes[root].lchild) + leafNum(self, self.nodes[root].rchild)
        if self.nodes == []:
            return 0
        else:
            return leafNum(self, self.root)
    
    def Show(self):
        def show(self, root, layer):
            if root == -1 or self.nodes[root] == -1:
                print('')
                return
            show(self, self.nodes[root].lchild, layer+1)
            for i in range(layer):
                print("   ", end = '')
            print(self.nodes[root].value)
            show(self, self.nodes[root].rchild, layer+1)
        if self.nodes == []:
            return
        else:
            show(self, self.root, 1)
        
    def Traverse(self, mode = 'm'):
        def traverse(self, root, mode):
            if root == -1 or self.nodes[root] == -1:
                return
            if mode == 'm':# l->d->r
                traverse(self, self.nodes[root].lchild, 'm')
                print(self.nodes[root].value, ' ', end = '')
                traverse(self, self.nodes[root].rchild, 'm')
            elif mode == 'l':# d->l->r
                print(self.nodes[root].value, ' ', end = '')
                traverse(self, self.nodes[root].lchild, 'l')
                traverse(self, self.nodes[root].rchild, 'l')
            else:# l->r->d
                traverse(self, self.nodes[root].lchild, 'r')
                traverse(self, self.nodes[root].rchild, 'r')
                print(self.nodes[root].value, ' ', end = '')
        if self.nodes == []:
            return
        else:
            traverse(self, self.root, mode)
    
    def Create(self):
        self.root = self.makeNode()
        print('create a tree, input the nodes in d->l->r \
              (parent->children->sibling for a tree or forest) sequence input . to stands for null')
        def create(self, pos, p):
                v = input("please input a character(. stands for a null node):")
                if v == '.':
                    self.nodes[pos] = -1
                    if self.nodes[p].lchild == pos:
                        self.nodes[p].lchild = -1
                    else:
                        self.nodes[p].rchild = -1
                    return
                self.nodes[pos].value = v
                self.nodes[pos].parent = p
                self.nodes[pos].address = pos
                self.nodes[pos].lchild = self.makeNode()
                create(self, self.nodes[pos].lchild, pos)
                self.nodes[pos].rchild = self.makeNode()
                create(self, self.nodes[pos].rchild, pos)
        create(self, self.root, -1)
        
    def Find(self, v):
        def find(self, root, v):
            if root == -1 or self.nodes[root] == -1:
                return -1
            if self.nodes[root].value == v:
                return root
            else:
                if find(self, self.nodes[root].lchild, v) != -1:
                    return find(self, self.nodes[root].lchild, v)
                else:
                    return find(self, self.nodes[root].rchild, v)
        if self.nodes == []:
            return -1
        else:
            return find(self, self.root, v) 
        
    def Root(self):
        if self.nodes == []:
            return -1
        return self.nodes[self.root]
    
    # add value in the child node of nodes[pos] 
    def add(self, p, v, mode = 'l'):
        pos = self.Find(p)
        if pos == -1:
            print('ERROR:', p, "is not in the tree, add it first!")
            return
        address = self.makeNode()
        self.nodes[address].address = address
        self.nodes[address].value = v
        self.nodes[address].parent = pos
        if mode == 'l':
            self.nodes[address].lchild = self.nodes[pos].lchild
            if self.nodes[pos].lchild != -1:
                self.nodes[self.nodes[pos].lchild].parent = address
            self.nodes[pos].lchild = address
        else:
            self.nodes[address].rchild = self.nodes[pos].rchild
            if self.nodes[pos].rchild != -1:
                self.nodes[self.nodes[pos].rchild].parent = address
            self.nodes[pos].rchild = address            

    def priorNode(self, v, mode = 'm'):
        pos = self.Find(v)
        if pos == -1:
            print("ERROR:", v, 'is not in the tree')
            return
        if mode == 'm':# l->d->r
            # if it has a left child tree 
            # the prior node is the rightmost node of the left child tree
            if self.nodes[pos].lchild != -1:
                prior = self.nodes[pos].lchild
                while self.nodes[prior].rchild != -1:
                    prior = self.nodes[prior].rchild
                return self.nodes[prior]
            # the node has no lchild and no parent
            if pos == self.root:
                return -1
            # the node has no lchild but it is not the root node
            prior = pos
            while self.nodes[self.nodes[prior].parent].lchild == prior:
                prior = self.nodes[prior].parent
                if prior == self.root:
                    return -1
            return self.nodes[self.nodes[prior].parent]
        elif mode == 'l':# d->l->r
            if pos == self.root:
                return -1
            # the node is the lchild of its parent
            if self.nodes[self.nodes[pos].parent].lchild == pos:
                return self.nodes[self.nodes[pos].parent]
            # the node is the rchild of its parent but the parent has no lchild
            if self.nodes[self.nodes[pos].parent].lchild == -1:
                return self.nodes[self.nodes[pos].parent]
            # the node is the rchild of its parent that has both lchild and rchild
            # go to the rightmost node of its sibling tree
            prior = self.nodes[self.nodes[pos].parent].lchild
            while self.nodes[prior].rchild != -1:
                prior = self.nodes[prior].rchild
            return self.nodes[prior]
        else:# l->r->d
            # if the node has a rchild
            if self.nodes[pos].rchild != -1:
                return self.nodes[self.nodes[pos].rchild]
            # the node has no rchild but has a lchild
            if self.nodes[pos].lchild != -1:
                return self.nodes[self.nodes[pos].lchild]
            # the node has no child nodes and has no parent node
            if pos == self.root:
                return -1
            prior = pos
            while self.nodes[self.nodes[prior].parent].lchild == prior or\
                self.nodes[self.nodes[prior].parent].lchild == -1:
                prior = self.nodes[prior].parent
                if prior == self.root:
                    return -1
            return self.nodes[self.nodes[self.nodes[prior].parent].lchild]
            
    def nextNode(self, v, mode = 'm'):
        pos = self.Find(v)
        if pos == -1:
            print("ERROR:", v, 'is not in the tree')
            return    
        if mode == 'm':# l->d->r
            # if it has a rchild go to the leftmost node of its rchild
            if self.nodes[pos].rchild != -1:
                nextn = self.nodes[pos].rchild
                while self.nodes[nextn].lchild != -1:
                    nextn = self.nodes[nextn].lchild
                return self.nodes[nextn]
            if pos == self.root:
                return -1
            # check the parent node untill the node is the lchild of its parent
            nextn = pos
            while self.nodes[self.nodes[nextn].parent].rchild == nextn:
                nextn = self.nodes[nextn].parent
                if nextn == self.root:
                    return -1
            return self.nodes[self.nodes[nextn].parent]
        elif mode == 'l':# d->l->r
            if self.nodes[pos].lchild != -1:
                return self.nodes[self.nodes[pos].lchild]
            if self.nodes[pos].rchild != -1:
                return self.nodes[self.nodes[pos].rchild]
            if pos == self.root:
                return -1
            # check the parent node until the node is not the last child
            nextn = pos
            while self.nodes[self.nodes[nextn].parent].rchild == nextn or \
                self.nodes[self.nodes[nextn].parent].rchild == -1:
                    nextn = self.nodes[nextn].parent
                    if nextn == self.root:
                        return -1
            return self.nodes[self.nodes[self.nodes[nextn].parent].rchild]
        else:# l->r->d
            if pos == self.root:
                return -1
            # the node is the last child of its parent
            if pos == self.nodes[self.nodes[pos].parent].rchild or \
                self.nodes[self.nodes[pos].parent].rchild == -1:
                return self.nodes[self.nodes[pos].parent]
            # go to the leftmost node of its sibling
            nextn = self.nodes[self.nodes[pos].parent].rchild
            while self.nodes[nextn].lchild != -1:
                nextn = self.nodes[nextn].lchild
            return self.nodes[nextn]
    
    # delete a node from the tree but keep the d->l->r traverse sequence
    def delete(self, v):
        pos = self.Find(v)
        if pos == -1:
            return
        vTmp = v
        positions = []
        while self.nextNode(vTmp, 'l') != -1:
            positions.append(self.Find(vTmp))
            vTmp = self.nextNode(vTmp, 'l').value
        positions.append(self.Find(vTmp))
        for i in range(len(positions)-1):
            self.nodes[positions[i]].value = self.nodes[positions[i+1]].value
        if positions[-1] == self.root:
            self.root = -1
            self.nodes = []
            return
        if self.nodes[self.nodes[positions[-1]].parent].lchild == positions[-1]:
            self.nodes[self.nodes[positions[-1]].parent].lchild = -1
        else:
            self.nodes[self.nodes[positions[-1]].parent].rchild = -1
        self.nodes[positions[-1]] = -1

    # for a tree which has been threaded, many functions will have to be changed
    # because for this tree the lchild/rchild may not be the real lchild/rchild 
    '''
    def thread(self, mode = 'm'):
        for n in len(self.__nodes):
            if self.nodes[n].lchild == -1:
                self.nodes[n].lchild = self.priorNode(n.value, mode).address
                self.nodes[n].mark = 'l'
            if self.nodes[n].rchild == -1:
                self.nodes[n].rchild = self.nextNode(n.value, mode).address
                if self.nodes[n].mark == 'l':
                    self.nodes[n].mark = 'a'
                else:
                    self.nodes[n].mark = 'r'
    ''' 
        
# test
if __name__ == '__main__':
    tree = binaryTree()
    tree.Create()
    tree.Show()
    print("number of leaf nodes is:", tree.LeafNum, 'depth is:', tree.Depth)
    tree.Traverse(mode = 'm')# l->d->r   
    print('')
    tree.Traverse(mode = 'l')# d->l->r
    v = tree.Root()
    while tree.nextNode(v.value, mode = 'l') != -1:
        print(v.value, '->', end = '')
        v = tree.nextNode(v.value, mode = 'l')
    print(v.value)
    while tree.priorNode(v.value, mode = 'l') != -1:
        print(v.value, '<-', end = '')
        v = tree.priorNode(v.value, mode = 'l')
    print(v.value)        
    tree.Traverse(mode = 'r')# l->r->d
        
    for i in ['w','x']:
        tree.add(tree.Root().value, i)
        tree.Show()
        print("number of leaf nodes is:", tree.LeafNum, 'depth is:', tree.Depth)        
    for i in ['y','z']:
        tree.add(tree.Root().value, i, mode = 'r')
        tree.Show()
        print("number of leaf nodes is:", tree.LeafNum, 'depth is:', tree.Depth)          

    tree.delete('a')
    tree.Show()
    print("number of leaf nodes is:", tree.LeafNum, 'depth is:', tree.Depth)   
    tree.Traverse(mode = 'l')
    print('')
    