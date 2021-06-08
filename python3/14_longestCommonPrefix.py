class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        result: accepted
        solution: traverse all words char by char and obtain the longest common prefix
        runtime: O(len(min(strs))*len(strs)), space: O(1)
        """
        Min = float("inf")
        ans = ""
        for str in strs:
            Min = min(Min, len(str))
        for i in range(Min):
            cur = strs[0][i]
            for str in strs:
                if str[i] != cur:
                    return ans
            ans += cur
        return ans