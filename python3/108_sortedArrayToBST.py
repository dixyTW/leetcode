class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l, r):
            
            if l > r: 
                return None
            mid = (l+r)//2
            val = nums[mid]
            root = TreeNode(val)
            root.left, root.right = helper(l, mid-1), helper(mid+1, r)
            return root
        return helper(0, len(nums)-1)