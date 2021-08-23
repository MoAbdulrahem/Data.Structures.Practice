# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        # The idea here is that we won't change the nodes' values, but rather the arrow direction between the nodes
        # We would declare two variables: temp and prev; prev would point to the previous node so that we can set the new pointer to it, temp would point to the node that we're currently setting the pointer of, and head would be on the next node of the temp node.
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
        # return self.reverse_recursive(head)