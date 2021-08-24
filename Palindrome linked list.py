# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #get the length of the list
        length = 0
        cur = head
        while cur:
            length += 1
            cur= cur.next
        
        cur = head  #return the cur pointer to the start of the list
        
        # divide the list into two lists with head pointing to the first and cur pointing to the second
        prev = None
        for i in range(length//2):
            prev = cur
            cur = cur.next
        if prev != None:
            prev.next = None
        
        #edge case: the list has odd number of nodes
        if length % 2 == 1:
            cur = cur.next
        
        #reverse one of the lists so that the nodes would match the second list in case of palindrome list
        previous = None
        while head:
            temp = head
            head = head.next
            temp.next = previous
            previous = temp
            
        head = previous     #reset the head to previous

        #loop over all the nodes of the two lists and see if all of them match
        while head and cur:
            if head.val == cur.val:
                head, cur = head.next, cur.next
            else:
                return False
        return True
            