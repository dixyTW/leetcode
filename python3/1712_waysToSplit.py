class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """
        prefix sum + two pointers:
        First we iterate through all possible left subarrays.
        Based on the problem statement, we want the following condition to be True
        i = index of the end of the left subarray
        j = index of the end of the mid subarray
        preSum[i] <= preSum[j] - preSum[i] <= preSum[-1] - preSum[j]
        """
        mod = 10**9 + 7
        N = len(nums)
        preSum = [0 for _ in range(N+1)]
        ans = 0
        for i in range(1, N+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        j,k = 0,0
        for i in range(1,N-1):
            while j <= i or (j < N and 2*preSum[i] > preSum[j]):
                j += 1
            while k < j or (k < N and preSum[k] - preSum[i] <= preSum[-1] - preSum[k]): 
                k += 1
            ans += k-j
        
        return ans % mod 
        
        """
        result: TLE
        DFS
        """
        # N = len(nums) 
        # def dfs(i,lst):
        #     ans = 0
        #     if i == N and len(lst) == 3:
        #         return 1
        #     cur = 0
        #     for j in range(i, N):
        #         cur += nums[j]
        #         if not lst or cur >= lst[-1]:
        #             lst.append(cur)
        #             ans += dfs(j+1, lst)
        #             lst.pop()
        #     return ans
        # return dfs(0, [])
    
        