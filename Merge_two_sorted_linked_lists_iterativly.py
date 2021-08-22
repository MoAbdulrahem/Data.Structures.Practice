#Merge two sorted linked lists to create a single sorted linked list
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self, l1, l2):
        head = output = ListNode(0)
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                output.next = ListNode(l1.val)
                l1 = l1.next
            else:
                output.next = ListNode(l2.val)
                l2 = l2.next
            output = output.next
        if not l1:
            output.next = l2
        else:
            output.next = l1
        return head.next
        #Complexity should be O(n) where n is the length of the smallest of the two arrays