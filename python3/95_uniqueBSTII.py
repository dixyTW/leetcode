# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(nums):
            if not nums:
                return None
            lst = []
            for i, root in enumerate(nums):
                for left in helper(nums[:i]) or [None] :
                    for right in helper(nums[i+1:]) or [None]:
                        tree = TreeNode(root, left, right)
                        lst.append(tree)
            return lst
        nums = [i for i in range(1, n+1)]
        return helper(nums)