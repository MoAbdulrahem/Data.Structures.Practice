# Binary Search
# It can only be used on sorted lists
# Complexity: O(log(n))
# It looks for the item to be found in the middle of the list, if it was there, it returns it.
# If not, it checks if the item is greater or less than the required item.
# If it was greater than the required item, we discard the right side of the lest. If not we discard the left.

def binary_search(items_list,item):
    start = 0
    end = len(items_list)-1
#     tries = 0
    while start <= end:
#         tries += 1
        mid = (start+end)//2
        guess = items_list[mid]
#         print ("Try number " + str(tries))
        if guess == item:
            return mid
        if guess > item:
            end = mid - 1
        else:
            start = mid +1
    return None

# Testing

import random

def test_binary_search(test_list,no_of_tries,test_range):
    for i in range(no_of_tries):
        sample = random.randint(test_range[0],test_range[1])
        print('searching for ', sample, ' : index = ', binary_search(test_list,sample))
    

test_list = list(range(10,1000))
test_binary_search(test_list,5,[1,1000])
