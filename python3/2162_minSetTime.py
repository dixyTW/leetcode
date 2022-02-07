class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def convert(s):
            # converts time string into seconds
            if not s:
                return -1
            sec, minutes = int(s[:2][::-1]), int(s[2:][::-1]) if s[2:] else 0
            
            return sec+minutes*60
        
        q = deque([["", startAt, 0]])
        ans = float('inf')
        while q:
            time, pos, cost = q.popleft()

            #convert time, if time > target, skip
            curSec = convert(time)
            if curSec == targetSeconds:
                ans = min(cost, ans)
            elif curSec < targetSeconds and len(time) < 4:
                #try all ways
                for i in range(10):
                    if i != pos:
                        q.append([str(i)+time, i, cost+moveCost+pushCost])
                q.append([str(pos)+time, pos, cost+pushCost])
                
        return ans
                
        