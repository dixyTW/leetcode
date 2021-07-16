class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        result: AC
        dfs: prevent duplicates by choosing smaller elements first
        runtime: O((kn)^n), space: O(n^2)
        improvements: set up array index to eliminate lst slicing, use backtracking to save space
        """
        lst = [x for x in range(1, n+1)]
        self.ans = []
        def helper(cur, nums):
            if len(cur) == k:
                self.ans.append(cur)
                return
            for i, num in enumerate(nums):
                helper(cur+[num], nums[i+1:])
        helper([], lst)
        return self.ans