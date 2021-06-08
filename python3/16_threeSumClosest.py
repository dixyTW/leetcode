class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        result: accepted
        n-sum variation: using the same method as 3sum, instead of checking for if the sum equals zero, 
        we update the answer by keeping track which triplet is closest to target
        we no longer need to keep track of duplicate solutions as well
        runtime: O(n^2), space: O(1)
        """
        diff = float("inf")
        ans = float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            l = i +1
            r = len(nums)-1
            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                if diff > abs(Sum-target):
                    diff = abs(Sum-target)
                    ans = Sum
                if Sum > target:
                    r -= 1
                else:
                    l += 1
        return ans