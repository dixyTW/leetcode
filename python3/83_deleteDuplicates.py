# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        result: AC
        two pointer: have the fast pointer check for unique values and adjust the slow pointer to the fast pointer accordingly
        runtime: O(n), space: O(1)
        """
        dummy = ListNode()
        if not head:
            return head
        dummy.next = head
        slow, fast = head, head.next
        while slow and fast:
            if slow.val == fast.val:
                prev = fast.val
                while fast and fast.val == prev:
                    fast = fast.next
                slow.next = fast
            else:
                slow, fast = slow.next, fast.next
        return dummy.next