class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        result: AC
        naive: get the number of 0,1,2s with first loop, then update on the second
        runtime: O(n), space: O(1)
        """
#         zero, one, two = 0, 0, 0
#         for num in nums:
#             if num == 0:
#                 zero += 1
#             elif num == 1:
#                 one += 1
#             else:
#                 two += 1
#         i = 0
#         while i < len(nums):
#             if zero:
#                 zero -= 1
#                 nums[i] = 0
#             elif one:
#                 one -= 1
#                 nums[i] = 1
#             else:
#                 two -= 1
#                 nums[i] = 2
#             i += 1 
        
        """
        dutch flag algorithm: 
        """
        zero = 0 #index for next zero insert position
        two = len(nums) - 1 #index for next two insert position
        i = 0 
        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1