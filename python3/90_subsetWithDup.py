class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        def helper(cur, lst):
            self.ans.append(cur)
            if not lst:
                return
            for i in range(len(lst)):
                if i > 0 and lst[i] == lst[i-1]:
                    continue
                helper(cur+[lst[i]], lst[i+1:])
                
                    
        helper([], nums)
        return self.ans