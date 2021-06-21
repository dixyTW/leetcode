class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        result: accepted
        dfs solution: same approach as Combination Sum I but we remove candidates from the lst once its used
        runtime: O(m^n) where m is length of candidate and n is target/min(candidate) (worst case)
        """
        self.ans = []
        candidates.sort()
        def helper(lst, cur, nums):
            if cur == target:
                self.ans.append(lst)
                return
            if cur > target:
                return 
            for i, num in enumerate(nums):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                helper(lst+[num], cur+num, nums[i+1:])
        helper([], 0, candidates)
        return self.ans