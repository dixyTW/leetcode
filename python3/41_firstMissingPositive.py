class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        source: https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
        result: accepted
        solution: 
        1. Get rid of all numbers that are not in the range 0-n-1 since they don't affect the solution
        2. We use the original array as a hash table to store numbers within the range 0 - n-1 (specifics in the 2nd for loop)
        3. We loop through the modified array, the index that contains less than len(nums) is the first missing positive, otherwise return len(n)
        runtime: O(n), space: O(1)
        
        """
        nums.append(0) #since arrays are 0 indexed, if an array contains all positive numbers 0... n-1, the array needs to be size n+1
        n = len(nums)
        for i in range(len(nums)):
            #remove all numbers that are not within range 0 - n
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[i]%n] += n
        for i in range(len(nums)):
            if nums[i]//n == 0:
                return i
        return n
                