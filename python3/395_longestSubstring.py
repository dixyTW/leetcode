class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        divide and conquer until a valid string appears
        """
        N = len(s)
        if not s:
            return 0
        counter = Counter(s) 
        
        flag = True
        for key in counter:
            if counter[key] < k:
                flag = False
        if flag:
            return N
        
        cur, start = 0, 0
        while cur < N:
            
            if counter[s[cur]] < k:
                return max(self.longestSubstring(s[start:cur], k), self.longestSubstring(s[cur+1:], k))
            cur += 1 
            