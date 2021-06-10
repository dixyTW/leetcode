# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        result: TLE
        naive solution: compare all lists at the same time and append the smallest value to the new list 
        runtime: O(n^2*M) where n is the number of lists and M as the length of a list
        """
        # head = dummy = ListNode(0)
        # finished = 0
        # while finished != len(lists):
        #     #cheks all linkedlist are traversed
        #     finished = 0
        #     Min = float('inf')
        #     index = 0
        #     for i, lst in enumerate(lists):
        #         #get the minimum values from the first value of all linkedlist
        #         if lst:
        #             if lst.val < Min:
        #                 Min = lst.val
        #                 index = i
        #         else:
        #             finished += 1
        #     if finished != len(lists):
        #         #move the pointer of the answer linked list and the linkedlist that was chosen
        #         dummy.next = lists[index]
        #         dummy = dummy.next
        #         lists[index] = lists[index].next
        # return head.next
        
        """
        result: accepted
        divide and conquer: 
        use a mergesort approach. Divide the lists into halves until all the lists become pairs.
        compare the two lists and merge into a sorted list
        repeat the processs untill one final sorted list is merged
        runtime: O(Mlog(n)) where M is the final length of the merged list and n as the number of lists, space: O(1)
        """
        # def merge(lst1, lst2):
        #     #merges 2 linked list and returns a sorted linkedlist
        #     dummy = ans = ListNode(0)
        #     while lst1 and lst2:
        #         val = 0
        #         if lst1.val > lst2.val:
        #             val = lst2.val
        #             lst2 = lst2.next
        #         else:
        #             val = lst1.val
        #             lst1 = lst1.next
        #         newNode = ListNode(val)
        #         dummy.next = newNode
        #         dummy = dummy.next
        #     dummy.next = lst1 or lst2
        #     return ans.next
        # if not lists:
        #     return None
        # if len(lists) == 1:
        #     return lists[0]
        # half = len(lists)//2
        # l = self.mergeKLists(lists[:half])
        # r = self.mergeKLists(lists[half:])
        # return merge(l,r)
        """
        result: accepted
        min heap:
        put all values into a min heap and construct a new LinkedList
        runtime: O(nlog(n)) where n is the total number of elements, space: O(n)
        """
        dummy = ans = ListNode(0)
        h = []
        for lst in lists:
            while lst:
                h.append(lst.val)
                lst = lst.next
        heapq.heapify(h)
        while h:
            newNode = ListNode(heapq.heappop(h))
            dummy.next = newNode
            dummy = dummy.next
        return ans.next