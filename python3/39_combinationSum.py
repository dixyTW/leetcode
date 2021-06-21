class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        result: accepted
        dfs solution: create a helper function that keeps track of the current lst
        cur lst are in ascending order so we can prevent duplicate answers
        runtime: O(m^n) where m is the length of candidates and n is target/min(candidates)
        """
        self.ans = []
        def helper(lst, cur, nums):
            
            if cur == target:
                self.ans.append(lst)
                return
            if cur > target:
                return
            for i, num in enumerate(nums):
                helper(lst+[num], cur+num, nums[i:])
        helper([], 0, candidates)
        return self.ans