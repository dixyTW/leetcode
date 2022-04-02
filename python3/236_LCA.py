# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node:
                return (None, 0)
            cnt, ret = 0, None
            if node == p or node == q:
                cnt += 1
            left_res, right_res = helper(node.left), helper(node.right)
            cnt += left_res[1]+right_res[1]
            ret = left_res[0] if left_res[0] else right_res[0]
            if cnt == 2 and not ret:
                ret = node
            return (ret, cnt)
        return helper(root)[0]