# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Min = -5001 #min number of input - 1
        def helper(lst, num):
            #helper function that inserts number to sorted list
            slow, fast = lst.next, lst.next.next
            temp = ListNode(num)
            if slow.val >= num:
                temp.next = slow
                lst.next = temp
                return
            while slow and fast and fast.val <= num:
                slow, fast = slow.next, fast.next
            if not fast:
                slow.next = temp
            else:   
                #num is in between slow and fast
                slow.next = temp
                temp.next = fast
                    
        ans = ListNode(None)
        ans.next = ListNode(head.val)
        head = head.next
        while head:
            helper(ans, head.val)
            head = head.next
        return ans.next