class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k):
            # returns number of subarray that contains less than or equal to k distinct ints
            N = len(nums)
            l, r = 0, 0 #window size
            dic = Counter() #distinct element within window 
            ans = 0
            while r < N:
                dic[nums[r]] += 1
                r += 1
                while l < r and len(dic) > k:
                    dic[nums[l]] -= 1
                    if dic[nums[l]] == 0:
                        del dic[nums[l]]
                    l += 1
                ans += r-l-1
            return ans
        return helper(k) - helper(k-1)
    
        