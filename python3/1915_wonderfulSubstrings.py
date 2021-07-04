class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        """
        source: https://leetcode.com/problems/number-of-wonderful-substrings/discuss/1299986/Python3-Bitwise-Explanation-or-O(n)
        result: accepted
        bitmask solution
        runtime: O(n)
        """
        seen = Counter()
        count = Counter()
        seen[0] = 1
        mask, ans = 0, 0
        for i, c in enumerate(word):
            bit = ord(c) - ord('a')
            count[c] += 1
            mask = mask ^ (1 << bit)
            ans += seen[mask]
            
            for j in range(10):
                if (1 << j) ^ mask in seen:
                    ans += seen[(1 << j)^mask]
            seen[mask] += 1
        return ans