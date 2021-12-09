class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        result: accepted
        merge sort: 
        runtime: O(nlogn), space: O(logn)
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        dummy = ans = ListNode(None)
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next 
        temp = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(temp)
        while l and r:
            if l.val > r.val:
                dummy.next = ListNode(r.val)
                dummy = dummy.next
                r = r.next
            else:
                dummy.next = ListNode(l.val)
                dummy = dummy.next
                l = l.next
        dummy.next = l if l else r
        return ans.next