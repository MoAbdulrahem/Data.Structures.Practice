# Selection Sort
# Complexity = O(n^2)
# We loop through the array and find the smallest (or largest) number.
# We append it to a new list and loop again to find the next item to be appended.

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

# Testing 

import random

def testing_selection_sort(input_range, list_max_length, no_of_tests):
    for i in range (no_of_tests):
        size = random.randint(1,list_max_length)
        test_list = []
        for i in range(size):
            
            test_list.append(random.randint(input_range[0],input_range[1]))
        print("Test Case   : " , test_list)
        print("Test Result : " , selection_sort(test_list),'\n')
            
testing_selection_sort([1,100],10,5)