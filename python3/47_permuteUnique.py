class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        result: accepted
        dfs solution: same approach as permutations I, but sort the lst first and eliminate duplicate numbers
        runtime: O(n!), space: O(n)
        """
        nums.sort()
        self.ans = []
        def helper(lst, cur):
            if not lst:
                self.ans.append(cur)
            for i in range(len(lst)):
                if i > 0 and lst[i-1] == lst[i]:
                    continue
                helper(lst[:i] + lst[i+1:], cur+[lst[i]])
        helper(nums, [])
        return self.ans