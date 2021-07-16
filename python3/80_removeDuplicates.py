class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        result: AC
        two pointer: i for traversing the list, index for next insert position
        runtime: O(n), space:O(1)
        """
        i = 1
        index = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                #when we see two repeated elements
                nums[index] = nums[i]
                index += 1
                i += 1
                while i < len(nums) and nums[i-1] == nums[i]:
                    i += 1
            else:
                nums[index] = nums[i]
                index += 1
                i += 1
        return index