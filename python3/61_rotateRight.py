# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        result: accepted
        solution: comments below
        runtime: O(n), space: O(1)
        """
        if not head:
            return head
        
        #get the length of the list
        leng = 1
        end = head
        while end.next:
            end = end.next
            leng += 1
        end.next = head
        #move pointer to the point where we want to modify    
        k = k%leng
        i = leng - k - 1
        dummy = head 
        while i > 0: 
            i -= 1
            dummy = dummy.next

        #move pointers
        ans = ListNode()
        ans.next = dummy.next
        dummy.next = None
        return ans.next