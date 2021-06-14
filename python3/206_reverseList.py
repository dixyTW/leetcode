# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        result: accepted
        solution: careful pointer manipulation
        runtime: O(n), space O(1)
        """
        prev = None
        while head:
            #visualization:
            #prev <- head <- head.next
            temp = head.next #next starting point (head)
            head.next = prev #keep 
            prev = head
            head = temp
        return prev