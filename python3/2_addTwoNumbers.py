# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Method: traverse both lst and keep track of carry bit
        Runtime: O(max(len(l1), len(l2))), Space: O(1)
        """
        carry = 0
        head = dummy = ListNode(0)
        while l1 or l2 or carry:
            #keep track of all three to eliminate individual checking, clean code and easy to maintain
            Sum = carry
            newNode = ListNode()
            if l1:
                Sum += l1.val
                l1 = l1.next
            if l2:
                Sum += l2.val
                l2 = l2.next
            carry, newNode.val = divmod(Sum, 10)
            dummy.next = newNode
            dummy = dummy.next
        return head.next