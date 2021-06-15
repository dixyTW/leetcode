class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        result: accepted
        binary search: binary search that inserts target into the left most possible position
        runtime: O(n), space: O(1)
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l