class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        """
        source: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/discuss/1298443/C%2B%2B-O(n)-one-pass-explained-multiple-solutions
        result: accepted
        pattern observation
        runtime: O(n), space: O(1)
        """
        chance = True
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev >= nums[i]:
                if not chance:
                    return False
                else:
                    chance = False
                    if i == 1 or nums[i] > nums[i-2]:
                        prev = nums[i]
                    #else: prev stays at nums[i-1], and we ignore nums[i]
            else:
                prev = nums[i]
                    
        return True