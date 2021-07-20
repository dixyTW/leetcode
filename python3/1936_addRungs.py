class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        height = 0
        ans = 0
        i = 0
        while i < len(rungs): 
            height = height + dist
            if height < rungs[i]:
                ans += 1 - int(not (rungs[i]-height)%dist) + (rungs[i] - height)//dist
            height = rungs[i]
            i += 1
            
        return ans
                