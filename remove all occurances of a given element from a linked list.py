# Remove all occurances of a given element from a linked list

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    # Time Complexity: O(N) 
    # Space Complexity: O(1) - It may appear that we created two extra lists so it should be O(N^2) but in fact, we created two references to the original linked list (two aliases for the same object in memory)
    def removeElements(self, head, val):
        cur = pointer = ListNode(None,head) # we added a new node at the beginning of the list so that we could start our comparison
        # from pointer.next and not from pointer => this is to cover the corner case where the first element of the list is equivilant to
        #to the element that we want to remove
        while pointer and pointer.next: # loop until the end
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return cur.next