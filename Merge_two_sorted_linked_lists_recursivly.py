#Merge two sorted linked lists to create a single sorted linked list
#Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self, l1, l2): 

        if not l1 or not l2: # This is the base case
            return l1 or l2
        if l1.val < l2.val: #Recursive case
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
