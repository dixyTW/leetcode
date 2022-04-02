# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        if root.left:
            root.left.val = 10*root.val + root.left.val
        if root.right:
            root.right.val = 10*root.val + root.right.val
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)
        
        # self.ans = []
        # def helper(node, cur):
        #     cur += str(node.val)
        #     if not node.left and not node.right:
        #         self.ans.append(cur)
        #         return
        #     if node.left:
        #         helper(node.left, cur) 
        #     if node.right:
        #         helper(node.right, cur)
        # helper(root, "")
        # return sum([int(x) for x in self.ans])