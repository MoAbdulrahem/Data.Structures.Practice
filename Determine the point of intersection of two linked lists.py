#Determine the Point of intersection of two linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        lenA, curA = 0 , headA
        lenB, curB = 0 , headB
        #get the number of nodes in the two lists
        while curA and curA.next:
            lenA += 1
            curA = curA.next
        while curB and curB.next:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB #reset the cur pointer to the heads of the lists
        #ignore the first elements in the longer list
        if lenA > lenB:
            for i in range(lenA-lenB):
                curA = curA.next
        else:
            for i in range(lenB-lenA):
                curB = curB.next
        
        # now we ignored the nodes that have 0 chance of intersection (i.e the nodes in one list and not the other)
        #checking for intersection
        while curA:
            if curA is curB:
                return curA
            else:
                # print(curA,curB)
                curA = curA.next
                curB = curB.next
        return None
                