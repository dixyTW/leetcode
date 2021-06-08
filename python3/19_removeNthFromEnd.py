# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        result: accepted
        naive: traverse the lst and get the position of the nth node, traverse the list again to edit the linkedlist
        runtime: O(n), space: O(1)
        """
        # leng = 0
        # ans = mod = ListNode(0)
        # mod.next = head
        # dummy = head
        # while dummy:
        #     leng += 1
        #     dummy = dummy.next
        # count = leng - n
        # while count > 0:
        #     mod = mod.next
        #     count -= 1 
        # mod.next = mod.next.next
        # return ans.next
        
        """
        result: accepted
        two pointer: use 2 pointers, fast and slow. 
        Let the fast pointer start at a position where when both fast and slow pointer start moving, and fast pointer is at the end of the list
        the slow pointer is at the correct position to edit the linkedlist (one node before the node we want to delete)
        runtime: O(n), space: O(1)
        """
        dummy = ListNode(0)
        fast = head
        dummy.next = head
        ans = slow = dummy
        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return ans.next