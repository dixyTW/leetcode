class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, min(N, 1)
        ans = 0
        while r < N:
            if nums[l] != nums[r]:
                l = r+1
                r += 2
            else:
                #delete num, increment index by 1
                r += 1
                ans += 1
        return ans if (N-ans)%2 == 0 else ans+1