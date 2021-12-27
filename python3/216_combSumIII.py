class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        how to prevent duplicates (same number, different number same sum)
        """
        nums = [i for i in range(1,10)]
        ans = []
        def dfs(nums, cur, lst):
            if cur < 0 or len(lst) > k:
                return
            if cur == 0 and len(lst) == k:
                ans.append(lst)
            else:
                for i, num in enumerate(nums):
                    dfs(nums[i+1:], cur-num, lst+[num])
            
        dfs(nums, n, [])
        return ans