# Check if a linked list has a cycle
#  1 --> 2 --> 3 --> 4 --/
#        ^--------------/
# a cyclic linked list would have the next pointer of a node pointing to a previous position on the list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        # Complexity would be O(n^2) as we would traverse the entire linked list and the entire visited array in worst case
        visited = [] # a list of the visited nodes
        while head and head.next:
            if head not in visited:
                visited.append(head)
                head = head.next
            else:
                return True
        return False
    
    # Another solution with O(n)
    def fast_has_cycle(self,head):
        """
        :type head: ListNode
        :rtype: bool
        
        The trick here is that we set any point we visited to None and then check 
        if we passed a point and found that its value is None then that point would've 
        been visited before.
        """
        while head:
            if head.val == None:
                return True
            head.val = None
            head = head.next
        return False
