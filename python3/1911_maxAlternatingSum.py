class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
        result: accepted
        DP solution
        runtime: O(n), space: O(n)
        """
        # even, odd = [0 for _ in range(len(nums)+1)], [0 for _ in range(len(nums)+1)]
        # for i in range(len(nums)):
        #     even[i+1] = max(even[i], odd[i]-nums[i])
        #     odd[i+1] = max(odd[i], even[i]+nums[i])
        # return max(even[-1], odd[-1])
        
        
        """
        improved version
        runtime: O(n), space: O(1)
        """
        even, odd = 0, 0
        for i in range(len(nums)):
            even, odd = max(odd-nums[i], even), max(even+nums[i], odd)
        return max(even, odd)