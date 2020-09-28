# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:19:40 2020

@author: 86156
"""

def countSort(l, minElem, maxElem):
    '''
    count sort
        count sort is a kind of linear sort
        create a new count list 
        count[index]: index is the rank of the element in all elements in the list
        the value of count[index] is the total number of this element in the list
    '''
    if isinstance(minElem, int) == False or isinstance(maxElem, int) == False:
        print('ERROR: please change the elements of the list into integers first!')
        return
    count = []
    for i in range(minElem, maxElem+1):
        count.append(0)
    for elem in l:
        count[elem-minElem] += 1
    newList = []
    for i in range(len(count)):
        j = 0
        while j < count[i]:
            newList.append(i)
            j += 1
    return newList
    
def radixSort(l):
    '''
    radix sort
        radix sort is a kind of linear sort
        sort from the last digit of the numbers 
        then compare the second last digit
        the compare the digit before it.....
        until all digits have been compared
    '''
    if isinstance(l[0], int) == False:
        print('ERROR: please change all the elements in the list into integers bigger than 0 first!')
        return
    newList = l
    base = 10
    while True:
        digit = []
        count = []
        for i in range(10):
            count.append([])
        mark = 0
        for i in range(len(newList)):
            digit.append(int(newList[i]%base/(base/10)))
            if digit[i] != 0:
                mark = 1
        if mark == 0:
            break
        for i in range(len(newList)):
            count[digit[i]].append(i)
        tmp = []
        for i in range(10):
            for index in count[i]:
                tmp.append(newList[index])
        newList = tmp
        print(newList)
        base = base*10  
    return newList