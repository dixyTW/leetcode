class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        brute force: 
        for every index i of nums, multiply multiply 
        all the other elements except for i
        runtime: O(n^2)
        """
        # ans = []
        # N = len(nums)
        # for i in range(N):
        #     n = 1
        #     for j in range(N):
        #         if j != i:
        #             n*=nums[j]
        #     ans.append(n)
        # return ans
        
        """
        prefix sum:
        1, 2, 6, 24
        24, 24, 12, 4
        """
        N = len(nums)
        pref_f = [1 for _ in range(N)]
        pref_b = [1 for _ in range(N)]
        ans = []
        for i in range(1, N):
            pref_f[i] = pref_f[i-1]*nums[i-1]
        for i in range(N-2, -1, -1):
            pref_b[i] = pref_b[i+1]*nums[i+1]
        for i in range(N):
            ans.append(pref_f[i]*pref_b[i])
        return ans
            