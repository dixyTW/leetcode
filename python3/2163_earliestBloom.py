class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        pairs = [(g,p) for g,p in zip(growTime, plantTime)]
        pairs = sorted(pairs, reverse=True)
        ans, cur = 0, 0
    
        for g,p in pairs:
            cur += p
            ans = max(ans, cur+g)
        return ans