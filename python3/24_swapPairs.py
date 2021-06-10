# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = ans = ListNode(0)
        prev.next = head
        while head and head.next:
            #original: prev -> one -> two -> newStart
            #after: prev -> two -> one -> newStart(head)
            one, two = head, head.next #easier to visualize
            newStart = head.next.next
            one.next = newStart
            two.next = one
            prev.next = two
            prev = head
            head = newStart
        return ans.next