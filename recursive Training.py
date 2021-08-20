#recursion Training
def sum_of_numbers_recursion(num):
    #we are required to print the sum of numbers from n to 1, i.e. n+(n-1)+(n-2)+......+3+2+1
    #base case is that we reached 1
    if num == 1: 
        return 1
    else:
        return num + sum_of_numbers_recursion(num-1)

def print_array_recursion(arr):
    #given an array, print it using recursion
    if len(arr) <2:
        return arr
    else:

        return [arr[0]]+print_array_recursion(arr[1:])

#Sum of digits of a given number using recursion
def sum_of_digits(num):
    '''
    we are given a number and required to use recursion to return the sum of digits of this number
    '''
    #base case: if the number consist of 1 digit
    number = str(num)
    if len(number) == 1:
        return int(number)
    else:
        temp = number[0]
        number = number[1:]
        return int(temp)+sum_of_digits(number)
    
#Sum of items within a list using recursion
def list_sum_by_recursion(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        return arr[0] + list_sum_by_recursion(arr[1:])