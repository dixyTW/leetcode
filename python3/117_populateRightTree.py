"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        dummy = root
        lst = [dummy]
        while lst:
            newLst = []
            for i in range(len(lst)):
                if i < len(lst)-1:
                    lst[i].next = lst[i+1]
                if lst[i].left:
                    newLst.append(lst[i].left)
                if lst[i].right:
                    newLst.append(lst[i].right)
            lst = newLst
            
            
        return root