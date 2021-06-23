class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        result: accepted
        dfs solution: search for each permutation recursively.
        runtime: O(n!*n) extra n for slicing lst, space: O(n)
        """
#         self.ans = []   
#         def helper(lst, cur):
#             if not lst:
#                 self.ans.append(cur)
#             for i, num in enumerate(lst):
#                 helper(lst[:i] + lst[i+1:], cur+[num])
#         helper(nums,[])
#         return self.ans
    
        
        """
        result: accepted
        backtrack solution: search recursively but eliminate the need for splicing by keeping track of what numbers are used using a set
        runtime: O(n!), space: O(n)
        """
        self.ans = []   
        def helper(cur, s):
            if len(cur) == len(nums):
                self.ans.append(cur)
                return
            for i in range(len(nums)):
                if nums[i] in s:
                    continue
                s.add(nums[i])
                helper(cur+[nums[i]], s)
                s.remove(nums[i])
        helper([], set())
        return self.ans