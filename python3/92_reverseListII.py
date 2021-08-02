# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse(node, count):
            #revese the given linkedlist and return its head and tail
            new_tail = node
            prev = None
            while count:
                count -= 1
                tmp = node.next
                node.next = prev 
                prev = node
                node = tmp
            node.next = prev
            return node, new_tail
        count = right - left
        dummy = prev = ListNode()
        prev.next = head
        fast = head
        while left > 1:
            prev = prev.next
            left -= 1
        while right > 1:
            fast = fast.next 
            right -= 1
        tmp = fast.next
        fast.next = None
        start, end = reverse(prev.next, count)
        prev.next = start
        end.next = tmp
        return dummy.next
        