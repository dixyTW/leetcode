class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # mem = [1 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j] and mem[i] < mem[j] + 1:
        #             mem[i] = mem[j] + 1
        # return max(mem)
        
        lst = []
        for num in nums:
            if len(lst) == 0 or lst[-1] < num:
                lst.append(num)
            else:
                index = bisect_left(lst, num)
                lst[index] = num
        return len(lst)
            
            