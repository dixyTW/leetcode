class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        result: accepted
        solution: iterate through the list and merge accordingly
        runtime: O(nlogn), space: O(n)
        """
        ans = []
        q = collections.deque(sorted(intervals))
        while len(q) >= 2:
            #seperation of functionality
            if q[0][1] >= q[1][0]:
                #edit the queue to make the intervals correct (no insertions)
                start = q[0][0]
                end = max(q[0][1], q[1][1])
                q.popleft()
                q.popleft()
                q.appendleft([start,end])  
            else:
                #only append new intervals into list here
                ans.append(q.popleft())
        while q:
            #handles left out intervals or in case of input that only has 1 interval
            ans.append(q.popleft())
        return ans