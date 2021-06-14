class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        result: accepted
        solution: 
        cases to consider
        1. if the lst is in descending order, reverse the lst to get the smallest permutation
        2. if the lst has a peak, find the peak, then find the index before the peak, that index
           is the number you want to swap out with the numbers on the right side of the index.
        3. starting from the least significant number (right most), find the first number that is greater than the number of index (nums[k] < nums[j])
        4. once swapped, we reverse the rest of the numbers after index (nums[l], nums[r] = nums[r], nums[l])
        runtime: O(n), space: O(1)
        """
        i = j = len(nums)-1
        while i-1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        k = i-1 #descending position
        while nums[k] >= nums[j]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1