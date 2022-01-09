class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones = nums.count(1)
        nums = nums + nums
        window, maxWindow = 0, 0
        for i in range(len(nums)):
            if i >= ones and nums[i-ones] == 1:
                window -= 1
            if nums[i] == 1:
                window += 1
            maxWindow = max(maxWindow, window)
        return ones - maxWindow
                