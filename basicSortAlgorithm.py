# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:17:27 2020

@author: 86156
"""

def insertSort(l):
    '''
    inserting sort
        go from the first element
        every new element will be insered into the new list
    '''
    newList = [l[0]]
    for element in l[1:]:
        pos = len(newList)
        for j in range(len(newList)):
            if newList[j] > element:
                pos = j
                break
        k = len(newList)
        newList.append(0)
        while k > pos:
            newList[k] = newList[k-1]
            k -= 1
        newList[pos] = element
    return newList
    
def selectSort(l):
    '''
    selection sort
        go from the minimum element
        add the second minimum element into the new list 
        add the next minimum element into the new list
        add ...... until all elements added
    '''
    newList = l
    start = 0
    while start < len(newList):
        pos = start
        for i in range(start, len(newList)):
            if newList[i] < newList[pos]:
                pos = i
        tmp = newList[start]
        newList[start] = newList[pos]
        newList[pos] = tmp
        start += 1
    return newList

def merge(l1, l2):
    '''
    merge two sorted list to make a new sorted list
    '''
    i = 0
    j = 0
    l = l1 + l2
    pos = 0
    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            l[pos] = l2[j]
            pos += 1
            j += 1 
        else:
            l[pos] = l1[i]
            pos += 1
            i += 1
    if j < len(l2):
        l[pos:] = l2[j:]
    elif i < len(l1):
        l[pos:] = l1[i:]
    return l    
def mergeSort(l, choice = 'u'):
    '''
    merge sort
        up-to-down mode:
        split the list into two lists, sort the two lists then merge them
        use recursion to conduct this algorithm
        down-to-up mode:
        merge every 2 elements in sequence
        the merge every 4 elements in sequence......
        until all elements merged into a new list
    '''
    if len(l) == 0:
        return l
    if len(l) == 1:
        return l
    if len(l) == 2:
        return merge(l[0:1], l[1:])
    if choice == 'u':
        l1 = mergeSort(l[0:int(len(l)/2)], choice)
        l2 = mergeSort(l[int(len(l)/2):], choice)
        return merge(l1, l2)
    else:
        length = 2
        while length/2 < len(l):
            for i in range(int(len(l)/length) + 1):
                l[length*i:length*(i+1)] = merge(l[length*i:int(length*i + length/2)], l[int(length*i + length/2):length*(i+1)])
                print(l[length*i:length*(i+1)])
            length = length * 2
        return l
    
def shellSort(l, step):
    '''
    Shell's sort
        pick elements in form of every 'step' elements and sort them
        then choose a smaller N and sort
        until step = 1
    '''        
    if step > len(l):
        print('ERROR: the step', step, 'is too much!')
        return
    newList = l
    while step > 0:
        start = 0
        while start < step:
            tmp = []
            i = 0
            while start + i*step < len(newList):
                tmp.append(newList[start + i*step])
                i += 1
            tmp = insertSort(tmp)
            i = 0
            while start + i * step < len(newList):
                newList[start + i*step] = tmp[i]
                i += 1
            start += 1
        step = int(step/2)
    return newList