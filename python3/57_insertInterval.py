class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        result: accepted
        use solution from merge interval but append the new interval at the very start
        runtime: O(nlogn), space: O(n)
        """
        # ans = []
        # intervals.append(newInterval)
        # q = collections.deque(sorted(intervals))
        # while len(q) >= 2:
        #     #seperation of functionality
        #     if q[0][1] >= q[1][0]:
        #         #edit the queue to make the intervals correct (no insertions)
        #         start = q[0][0]
        #         end = max(q[0][1], q[1][1])
        #         q.popleft()
        #         q.popleft()
        #         q.appendleft([start,end])  
        #     else:
        #         #only append new intervals into list here
        #         ans.append(q.popleft())
        # while q:
        #     #handles left out intervals or in case of input that only has 1 interval
        #     ans.append(q.popleft())
        # return ans
        """
        result: accepted
        tricky solution: 
        runtime: O(n), space: O(n)
        """
        ans = []
        for intv in intervals:
            """
            1. insert intv into ans
            2. modify newIntv
            - insert (insert newInterval, replace newInterval)
            - no insert (modify newInterval)
            """
            if intv[1] < newInterval[0]:
                ans.append(intv)
            elif intv[0] <= newInterval[0] <= intv[1] or newInterval[0] <= intv[0] <= newInterval[1]:
                newInterval[0], newInterval[1] = min(intv[0], newInterval[0]), max(intv[1], newInterval[1])

            elif intv[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = intv
        ans.append(newInterval)
        return ans