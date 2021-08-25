class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        dic = set()
        for num in nums:
            bi = int(num, 2)
            dic.add(bi)
        start = 0
        Max = 2**len(nums[0]) + 1 
        while start <= Max:
            if start not in dic:
                return "{0:b}".format(start).zfill(len(nums[0]))
            start += 1