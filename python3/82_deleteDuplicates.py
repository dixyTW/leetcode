# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        result: AC
        two pointer: prev pointer that connects all unique value, only modify prev pointer if we are certain there are no duplicates
        runtime: O(n), space: O(1)
        """
        dummy = prev = ListNode()
        while head and head.next:
            if head.val == head.next.val:
                val = head.val
                while head and head.val == val:
                    #bypass all duplicate values 
                    head = head.next
            else:
                prev.next = head
                prev = prev.next
                head = head.next
        prev.next = head if head else None
        return dummy.next