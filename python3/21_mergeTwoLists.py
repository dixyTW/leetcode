# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        result: accepted
        solution: traverse both list at the same time, compare 2 pointer's value
        append the smaller value to the new list
        remember to append the remaining list to the end of the new lst
        runtime: O(l1+l2), space: O(1)
        """
        ans = ListNode(0)
        dummy = ans 
        while l1 and l2:
            val = 0
            if l1.val > l2.val:
                val = l2.val
                l2 = l2.next
            else:
                val = l1.val
                l1 = l1.next
            newNode = ListNode(val)
            ans.next = newNode
            ans = ans.next
        ans.next = l1 if l1 else l2
        return dummy.next