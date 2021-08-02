class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        """
        result: TLE
        DFS
        runtime: O(2^n)
        """
        # def dfs(prev, i):
        #     if prev == nums[i] or prev+1 == nums[i]:
        #         if nums[i] == 2:
        #             self.ans += 1 
        #         prev = nums[i]
        #     else:
        #         return
        #     for index in range(i+1, len(nums)):
        #         dfs(prev, index)
        # self.ans = 0
        # for i in range(len(nums)-2):
        #     dfs(-1, i)
        # return self.ans
        
        """
        DP: mem[3][3] = at index 2, the string has x number of subsequences that ends at 2
        runtime: O(3*N)
        """
        mem = [[0 for _ in range(4)] for _ in range(len(nums)+1)]
        for r in range(len(nums)):
            mem[r][0] = 1
        for r in range(len(nums)):
            for c in range(3):
                if nums[r] == c:
                    mem[r+1][c+1] = mem[r][c] + mem[r][c+1]*2
                else:
                    mem[r+1][c+1] = mem[r][c+1]
        return mem[-1][-1] % (10**9 + 7)
                    