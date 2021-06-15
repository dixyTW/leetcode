class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        solution: accepted
        binary search: run 2 binary search, one that finds the left most element, the other the right most
        runtime: O(log(n)), space: O(1)
        """
        left = self.left_search(target, nums)
        right = self.right_search(target, nums)
        return [left, right] if left <= right else [-1, -1]       
        
    def left_search(self, target, nums):
        #helper function that searches the leftmost target
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l
    
    def right_search(self, target, nums):
        #helper function that searches the rightmost target 
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= target:
                l = mid+1
            else:
                r = mid-1
        return r