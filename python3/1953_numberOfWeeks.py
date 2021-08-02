class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        if len(milestones) == 1:
            return 1
        milestones.sort() #didn't need to sort, just get the max value
        Sum = sum(milestones)
        ans = 0
        for i in range(len(milestones)-1):
            ans += milestones[i]
        return min(ans*2+1, milestones[-1]+ans)