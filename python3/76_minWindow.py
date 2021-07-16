class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        source: official leetcode solution
        sliding window: 
        core idea: expand with the right index, and contract with left index
        runtime: O(n) #2S, space: O(s+t)
        """
        count_t = collections.Counter(t)
        l, r = 0, 0
        match = len(count_t)
        s_match = 0
        count_s = collections.Counter()
        Min = float('inf')
        start = 0
        while r < len(s):
            count_s[s[r]] += 1
            if count_s[s[r]] == count_t[s[r]]:
                s_match += 1
            while r-l+1 >= len(t) and s_match == match:
                if r-l+1 < Min:
                    Min = r - l + 1
                    start = l
                
                count_s[s[l]] -= 1
                if count_s[s[l]] < count_t[s[l]]:
                    s_match -= 1
                l += 1
            r += 1
        return s[start:start+Min] if Min != float('inf') else ""
                