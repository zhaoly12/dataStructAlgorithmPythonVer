# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:19:01 2020

@author: 86156
"""

from ipdb import set_trace

def fastSort(array):
    '''
    fast sort:
        see the first element as the target element
        define two cursors l, h
        l-1 points at the last element that no smaller than target element
        h+1 points at the first element that bigger than target element
        move l and h until l > h
        check start~h-1 and h+1~end (use recursion)
    '''
    if len(array) == 1 or len(array) == 0:
        return array
    l = 1
    h = len(array) - 1
    target = array[0]
    while l < len(array) and array[l] <= target:
        l += 1
    while h > 0 and array[h] > target:
        h -= 1
    while l <= h:
        if array[h] > target:
            h -= 1
        else:
            tmp = array[l]
            array[l] = array[h]
            array[h] = tmp
            l += 1
    tmp = array[h]
    array[h] = target
    array[0] = tmp
    array[0:h] = fastSort(array[0:h])
    array[h+1:] = fastSort(array[h+1:])
    return array
    
def fillSort(array):
    '''
    fill sort:
        see the first element as the target element and pick it out
        define two cursors l, h
        l points at the start point of the array(the first empty position)
        h points at the end point of the array
        move h until array[h] <= target
        fill empty position with this value, then h will be the new empty position
        move l until array[l] > target
        fill empty position with this value, then l will be the new empty position
        move h.......
        until l >= h
        check start~l-1 and l+1~end (use recursion)
    '''
    if len(array) == 1 or len(array) == 0:
        return array
    target = array[0]
    l = 0 
    h = len(array) - 1
    while True:
        while array[h] > target:
            h -= 1
        if l < h:
            array[l] = array[h]
        else:
            break
        while True:
            l += 1
            if l == h:
                break
            if array[l] > target:
                break
        if l < h:
            array[h] = array[l]
        else:
            break
    array[l] = target
    array[0:l] = fillSort(array[0:l])
    if l < len(array)-1:
        array[l+1:] = fillSort(array[l+1:])
    return array
    
def DijkstraSort(array):
    '''
    Dijkstra sort:
        see the first element as the target element
        define three cursors l,m,h
        l points at the first element that equals to the target element
        m-1 points at the last element that equals to the target element
        h+1 points at the first element that is bigger than the target element
        move cursors until m > h
        check start~l-1 and h+1~end (use recursion)
    '''
    target = array[0]
    l = 0
    m = 1
    h = len(array)-1
    while m <= h:
        if target < array[h]:
            h -= 1
        elif target == array[h]:
            tmp = array[m]
            array[m] = array[h]
            array[h] = tmp
            m += 1
        else:
            tmp = array[m]
            array[m] = array[l]
            #### ! be carful here!
            if m != h:
                array[l] = array[h]
                array[h] = tmp
            else:
                array[l] = tmp
            l += 1
            m += 1
    if 0 <  l-1:
        array[0:l] = DijkstraSort(array[0:l])
    if h + 1 < len(array)-1:
        array[h+1:] = DijkstraSort(array[h+1:])
    return array

def heapSort(array):
    '''
    heap sort:
        use data in the array to build a binary tree and make sure value of the parent node
        is no less than the values of its child nodes
        store values in a new array. array[k] is the parent node, array[2*k] is the left child
        and array[2*k+1] is the right child, array[1] is the root node, array[0] is empty
        swap the last element of this new array and array[1]
        for array[0:len(array)-1] sink array[1] down to the right position 
        then do the same procedure until array[0:end] end <= 1
    '''
    if len(array) == 1 or len(array) == 0:
        return array
    array += ['start']
    tmp = array[0]
    array[0] = array[len(array)-1]
    array[len(array)-1] = tmp
    # build the heap
    p = int((len(array)-1)/2)
    end = len(array) - 1
    while p > 0:
        pos = p
        while pos <= end:
            maxPos = pos
            if 2*pos <= end:
                if array[2*pos] > array[pos]:
                    maxPos = 2 * pos
            if 2*pos + 1 <= end:
                if array[2*pos+1] > array[maxPos]:
                    maxPos = 2 * pos + 1
            if maxPos == pos:
                break
            else:
                tmp = array[pos]
                array[pos] = array[maxPos]
                array[maxPos] = tmp
            pos = maxPos
        p -= 1
    # swap data and update the heap
    while True:
        tmp = array[1]
        array[1] = array[end]
        array[end] = tmp
        end -= 1
        if end == 1:
            break
        # update the heap
        pos = 1
        while pos <= end:
            maxPos = pos
            if 2*pos <= end:
                if array[2*pos] > array[pos]:
                    maxPos = 2 * pos
            if 2 * pos + 1 <= end:
                if array[2*pos+1] > array[maxPos]:
                    maxPos = 2*pos+1
            if maxPos == pos:
                break
            else:
                tmp = array[pos]
                array[pos] = array[maxPos]
                array[maxPos] = tmp
            pos = maxPos
    return array[1:]
    