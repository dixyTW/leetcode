class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        result: TLE
        naive solution: create all combinations of triplets and check for the sum
        runtime: O(n^3 * len(ans)), space: O(1)
        """
        # ans = []
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 lst = [nums[i], nums[j], nums[k]]
        #                 lst.sort() #sort the lst so we can check for duplicates
        #                 if lst not in ans:
        #                     ans.append([nums[i],nums[j],nums[k]])
        # return ans
        """
        result: accepted
        generic N Sum solution:
        we try all combinations of triplets by sorting the list first,
        this will allow us to have control of our Sum value while we itterate through the list
        it is import to prevent duplicates for all three indexes
        runtime: O(n^2), space: O(1)
        """
        nums.sort()
        ans = [] 
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                if Sum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif Sum > 0:
                    r -= 1
                else:
                    l += 1
        return ans