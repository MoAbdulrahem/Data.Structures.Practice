#Maximum Pair Wise
#Input two lines:
#1st is the number of inputs
#second is a sequesnce of numbers
#It's required to return the result of multiplying the two largest numbers
def max_pair_wise():
    no_of_lines = input ()
    seq = input()

    largest = 0
    second_largest = 0
    for i in seq.split():
        if int(i) > largest:
            second_largest = largest
            largest = int(i)

    print(largest * second_largest) 


# Stress Testing
import random
# i = 0
# while i < 20:
#     i+= 1
#     lines = random.randint(2,10)
#     sequence = ""
#     for i in range(lines):
#         sequence += str(random.randint(0,10)) + ' '
#     print (sequence)
#     max_pair_wise(sequence)

max_pair_wise()