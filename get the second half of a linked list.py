# Given a linked list, determine the middle element and return the second half of the linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        #get the length of the linked list
        length = 0 
        cur = head
        while cur:
            length += 1
            cur = cur.next
            
        cur = head
        
        if length % 2 == 0:
            for i in range((length//2)):
                cur = cur.next
        else:
            for i in range((length//2)):
                cur = cur.next
        return cur
    
    # another solution using two pointers
    def middleNode2(self, head):
        '''
        One pointer is pointing directly at the next node and the other on the node after the next, so when the latter pointer
        reaches the end of the linked list, the first pointer would be just at the middle
        '''
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head