import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #naive solution: try every possible pair of solutions
        #runtime: O(n^2), space: O(1)
        #run 2 indexes (i,j) with 2 for loops and add the two numbers together
        #and check if their sum equals target
        #skip if i == j since you can't use the same element twice
        """
        for i in range(len(nums)):
            #we don't care about duplicate pairs here 
            #i.e (num[i], num[j]), (num[j], num[i])
            #since it does not go against the rules
            for j in range(len(nums)):
                if i == j:
                    pass
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
        """
    
        #map (dictionary) solution: 
        #runtime: O(n), space: O(n)
        dic = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if num in dic:
                return [i, dic[num]]
            dic[target-num] = i
        return []