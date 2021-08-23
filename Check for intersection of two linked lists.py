# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def getIntersectionNode(self, headA, headB):
        # This solution runs in O(N) time complexity and O(1) space complexity
        # If two linked lists intersected at any point, then both of them would have the same tail node, regradeless of the position of intersection.
        while headA and headA.next: #get the tail of the first list
            headA = headA.next
        while headB and headB.next:# get the tail of the second list
            headB = headB.next
        if headA is headB : #if both the tails are the same object
            return True
        else:
            return False