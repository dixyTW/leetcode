class Solution:
    def numTrees(self, n: int) -> int:
        """
        result: TLE
        brute force DFS: unique structure of a BST tree = unique structure of the left subtree * unique structure of the right subtree
        runtime: O(n!), space
        """
#         def helper(lst, l, r): 
#             if not lst:
#                 return 1
#             ans = 0
#             for i, root in enumerate(lst):
#                 if l < root < r:
#                     ans += helper(lst[:i], l, min(root,r)) * helper(lst[i+1:], max(l,root), r)
#             return ans
#         if not n:
#             return 0
#         nums = [i for i in range(1, n+1)]
#         return helper(nums, float('-inf'), float('inf'))
#         #simple version
#         if n == 0:
#             return 1
#         res = 0
#         for i in range(n):
#             res += self.numTrees(i)*self.numTrees(n-1-i)
#         return res 
        """
        result: AC
        memoization solution
        runtime: O(n^2)
        """
        # @lru_cache
        # def helper(n):
        #     if n == 0:
        #         return 1
        #     res = 0
        #     for i in range(n):
        #         res += helper(i)*helper(n-1-i)
        #     return res 
        # return helper(n)
        """
        result: AC
        DP solution:
        """
        mem = [0 for _ in range(n+1)]
        mem[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                mem[i] += mem[j-1]*mem[i-j]
        return mem[-1]