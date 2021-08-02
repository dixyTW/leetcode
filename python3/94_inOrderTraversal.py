# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #recursive
#         def helper(node, lst):
#             if node:
#                 helper(node.left, lst)
#                 lst.append(node.val)
#                 helper(node.right, lst)   
#         ans = []
#         helper(root, ans)
#         return ans
        
        #iterative
        stack = []
        ans = []
        while root or stack:
            if not root:
                root = stack.pop()
                ans.append(root.val)
                root = root.right
            else:
                stack.append(root)
                root = root.left
        return ans