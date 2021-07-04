class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        result: TLE
        naive solution: try every path
        runtime: O(n^2), space: O(n)
        """
        # mem = [False for _ in range(len(nums))]
        # mem[0] = 1
        # for i, boo in enumerate(mem):
        #     if boo:
        #         for j in range(1, nums[i]+1):
        #             if i+j >= len(nums):
        #                 break
        #             mem[i+j] = True
        # return mem[-1]
        
        """
        result: accepted
        greedy solution: keep track of the current longest jump and only update the longest jump if we can reach the current index
        runtime: O(n), space: O(1)
        """
        furthest = 0
        for i, num in enumerate(nums):
            if furthest >= i:
                furthest = max(furthest, i+num)
        return furthest >= len(nums)-1