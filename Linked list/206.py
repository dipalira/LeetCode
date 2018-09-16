# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None 
        while head:
            #Where current elements points to
            curr = head.next
            head.next = prev
            prev = head
            #Current is the next of current head
            head = curr
        return prev
