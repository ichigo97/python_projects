# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:44:27 2021

@author: Ananthu
"""

def bubblesort(array):
    """Function that performs bubble sort on given input list"""
    
    for i in range(len(array)-1, 0, -1): # reverse iteration to fix the topmost/right most value
        for j in range(i): 
            if array[j] > array[j+1]: # checks current value as highest 
#                array[j],array[j+1] = array[j+1], array[j]
                # swap with right value
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp 
    return array


if __name__ == '__main__':
    array = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53] # input to the fn
    print("Before Sorting", array)
    print("After Sorting", bubblesort(array))
    