class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        N = len(nums)
        while i < N:
            start = end = i
            while end < N - 1 and nums[end+1] == nums[end] + 1:
                end += 1
            ans.append(str(nums[start]) + ("->" + str(nums[end]))*(start!=end))
            i = end + 1
        return ans