class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        result: TLE
        naive solution: get the sum of every subarray
        runtime: O(n^2), space: O(1)
        """
        # ans = float('-inf')
        # for i in range(len(nums)):
        #     Sum = 0
        #     for j in range(i, len(nums)):
        #         Sum += nums[j]
        #         ans = max(ans, Sum)
        # return ans 
        
        """
        result: accepted
        DP solution (Kadane's Algorithm)
        runtime: O(n), space: O(n)
        """
        mem = [0 for _ in range(len(nums))] #mem[i] represents max subarray endding at index i
        mem[0] = nums[0]
        for i in range(1, len(nums)):
            mem[i] = nums[i] + max(0, mem[i-1])
        return max(mem)
                 
        """
        result: accepted
        Kadane's Algorithm: constant space
        runtime: O(n), space: O(1)
        """
        # for i in range(1, len(nums)):
        #     if nums[i-1] > 0:
        #         nums[i] += nums[i-1]
        # return max(nums)