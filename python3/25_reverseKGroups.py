class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        result: accepted
        reverse linkedlist solution: 
        We use the reverse linkedlist algorithm as a helper function. Instead of reversing the entire linkedlist, we use a counter as the end condition
        runtime: O(n), space: O(1)
        """
        def reverse(node):
            #helper function to reverse linkedlist of length k
            prev = None
            count = 0
            while count != k:
                count += 1
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                
            return prev
        if k == 1:
            return head
        """
        case 1: no edit (k ==1 )
        case 2: one cycle(len(n) < 2k)
        case 3: two or more cycle (len(n) > (2+)k)
        """
        ans = dummy = ListNode()
        while head:
            count = 0
            start = head 
            while head and count < k:
                count += 1
                head = head.next
            if count == k:
                ret = reverse(start)
                dummy.next = ret
                dummy = start #move to the end of reversed lst
            else:
                dummy.next = start
        return ans.next