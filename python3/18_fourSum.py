class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        result: Accepted
        n Sum solution: reduce the problem into a 2 sum problem 
        runtime: O(n^3), space: O(1)
        """
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    #avoid skipping the first check and duplicate numbers
                    continue
                l = j+1
                r = len(nums)-1
                while l < r:
                    Sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if Sum == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif Sum > target:
                        r -= 1
                    else:
                        l += 1
        return ans