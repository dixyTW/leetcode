class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        result: accepted
        runtime: O(n^2), space: O(n^2)
        """
        if len(points) <= 1:
            return len(points)
        dic = collections.defaultdict(set) #key: (slope, x, y) x,y intersection on the y axis
        seen = set() #prevent duplicates
        ans = 0
        for i in range(len(points)):
            comp_p = points[i] #comparison point relative to points[j]
            for j in range(len(points)):
                if (i,j) not in seen and (j,i) not in seen and i != j:
                    seen.add((i,j))
                    slope = float('inf')
                    key = None
                    if points[i][0] != points[j][0]:
                        slope = (points[i][1] - points[j][1])/(points[i][0] - points[j][0])
                    if slope == 0:
                        key = (slope, 0, points[j][1])
                    elif slope == float('inf'):
                        key = (slope, points[i][0], 0)
                    else:
                        key = (slope, 0, points[j][1]-points[j][0]*slope)
                    dic[key].add(i)
                    dic[key].add(j)
                    
        for key, val in dic.items():
            if len(val) > ans:
                ans = len(val)
        return ans