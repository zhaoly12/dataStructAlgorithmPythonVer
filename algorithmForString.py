# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:37:38 2020

@author: 86156
"""

def stringComparison():
    '''
    string comparison
        use least-significant-digit first(LSD) to compare different strings
        for example: bcc > bbc > acc > abd >  abc > abb
    '''
    print('compare strings with the same length')
    length = int(input('please input the length:'))
    strings = []
    while True:
        string = input("please input a string , input '-1' to end:")
        if string == '-1':
            break
        if length != len(string):
            print('ERROR: length should be', length)
            return
        strings.append(string)
    # main part
    # sort by digit
    def sortByDigit(strings, digit):
        collect = []
        tmp = []
        for string in strings:
            collect.append(string[digit])
            tmp.append('-1')
        # use count sort
        count = []
        minOrd = ord(min(collect))
        maxOrd = ord(max(collect))
        for i in range(maxOrd-minOrd+1):
            count.append(0)
        for char in collect:
            count[ord(char)-minOrd] += 1
        # generate indexes for characters
        # the index of character ord(char)-minOrd = i is from count[i-1] to count[i]-1
        for i in range(1, len(count)):
            count[i] = count[i] + count[i-1]
        starter = 0
        for pos in range(len(collect)):
            char = collect[pos]
            if ord(char)-minOrd == 0:
                index = starter
                starter += 1
            else:
                index = count[ord(char)-minOrd-1]
                count[ord(char)-minOrd-1] += 1
            tmp[index] = strings[pos]
        return tmp
    digit = length - 1
    while digit >= 0:
        strings = sortByDigit(strings, digit)
        print('sort by digit:', digit)
        for string in strings:
            print(string)
        digit -= 1
    print('done!')
        
def BF(string, substring):
    '''
    using brute force to judge if a string is the substring of another string
    '''
    pos = 0
    while True:
        index = pos
        if index > len(string) - len(substring):
            return False
        char = string[index]
        for i in range(len(substring)):
            if substring[i] != char:
                pos += 1
                break
            else:
                index += 1
                if i == len(substring) - 1:
                    return True
                char = string[index]

def KMP(string, substring):
    '''
    KMP algorithm
        when using brute force to compare two string, 
        every time we start from the first char of substring.
        KMP algorithm is an algorithm to find the best start point of substring
        the only difference between KMP and BF is the start point of substring
    ''' 
    # when substring[i] != string[pos] compare substring[next[i]] with string[pos]
    nextStart = []
    for i in range(len(substring)):
        nextStart.append(0)
    j = 0 # j is the tail of the prefix
    # i-1 is the tail of the suffix(prefix == suffix)
    for i in range(2, len(substring)):
        if substring[j] == substring[i-1]:
            # add new char substring[i-1] and change the prefix of substring[0:i-1]
            j += 1
            nextStart[i] = nextStart[i-1] + 1
        else:
            # add new char substring[i-1] and change the prefix of substring[0:i-1]            
            while j != 0:
                j = nextStart[j]
                if substring[j] == substring[i-1]:
                    break
            nextStart[i] = nextStart[j]
    # main part(almost the same with BF)
    stringStart = 0
    subStart = 0
    while True:
        pos = stringStart
        if stringStart > len(string) - len(substring):
            return False
        for i in range(subStart, len(substring)):
            if substring[i] != string[pos]:
                stringStart += 1
                subStart = nextStart[i]
                break
            else:
                pos += 1
                if i == len(substring) - 1:
                    return True
    