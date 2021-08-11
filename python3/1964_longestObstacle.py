class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        """
        runtime: O(nlogn), space: O(n)
        """
        ans = []
        lst = []
        for i, num in enumerate(obstacles):
            x = bisect.bisect(lst,num)
            ans.append(x+1)
            if x == len(lst):
                lst.append(num)
            else:
                lst[x] = num
        return ans