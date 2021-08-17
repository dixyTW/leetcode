class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = collections.defaultdict(bool)
        ans = 0
        for num in nums:
            dic[num] = False
        for num in nums:
            if num in dic and dic[num] == False:
                leng = 0
                while num in dic:
                    dic[num] = True
                    leng += 1
                    num += 1
                ans = max(ans, leng)
        return ans