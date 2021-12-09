class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0 
        for i in range(32):
            count = 0
            for num in nums:
                if num>>i:
                    count += 1
            single += (count%3)<<i
        return single if single < (1<<31) else single - (1<<32) #two