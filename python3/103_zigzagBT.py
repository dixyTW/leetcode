# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 
        reverse = False
        stack = [root]
        ans = []
        while stack:
            
            newStack = []
            lvl = []
            for _ in range(len(stack)):
                node = stack.pop()
                lvl.append(node.val)
                if reverse:
                    if node.right:
                        newStack.append(node.right)
                    if node.left:
                        newStack.append(node.left)
                else:
                    if node.left:
                        newStack.append(node.left)
                    if node.right:
                        newStack.append(node.right)
                    
            reverse = not reverse
            stack = newStack
            ans.append(lvl)
        return ans