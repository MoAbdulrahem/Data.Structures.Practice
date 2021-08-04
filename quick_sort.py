#Implementing Quick Sort
#Complexity: O(nlogn) for average and best cases
# O(n^2) for worst case

#Quick Sort uses divide and conquer technique
# to use divide and conquer we need to
# 1. detemine the base case; that is, the simplest possible case, for quick sort, it's an empty array of an array of 1 element
# 2. reduce the problem until it reaches the base case.

def quick_sort(arr):
    if len(arr) < 2:
        return arr  #This is the base case
    else:
        pivot = arr[0] #This is the recursive case, Choosing the pivot to be the first item in the list is a bad practice, as it would result in worst case runtime if the input was already sorted. However, we should choose an element in the middle of the list or a random element
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater) 


#testing quick sort
import random
def test_quick_sort(no_of_tests=10, max_list_size=20, input_range=[0,1000]):
    for i in range(no_of_tests):
        size = random.randint(1,max_list_size)
        test_list = []
        for i in range(size):
            test_list.append(random.randint(input_range[0],input_range[1]))
        print("Generated Test Case: ", test_list)
        expected_output = test_list
        expected_output.sort()
        print("Expected Output    : ", expected_output)
        print("Quick Sort Output  : ", quick_sort(test_list))
        print("="*20)
test_quick_sort()