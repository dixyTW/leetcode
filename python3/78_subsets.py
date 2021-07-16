class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        result: AC
        dfs: add everything to the answer
        runtime: O(n*2^n), space: O(2^n*n)
        """
        self.ans = []
        def helper(lst, cur):
            self.ans.append(cur)
            for i, num in enumerate(lst):
                helper(lst[i+1:], cur + [num])
        helper(nums, [])
        return self.ans