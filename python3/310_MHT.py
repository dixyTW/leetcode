class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def helper(lst):
            # returns max dist node
            ans, Max = 0, float('-inf')
            for i, e in enumerate(lst):
                if e > Max:
                    ans, Max = i, e
            return ans
        
        def dfs(cur, lst, visited, dist, graph):
            visited.add(cur)
            lst[cur] = dist
            dist += 1
            for node in graph[cur]:
                if node not in visited:
                    path[node] = cur
                    dfs(node, lst, visited, dist, graph)
            
        if n == 1:
            return [0]
        
        #graph building
        g = defaultdict(list)
        for fr, to in edges:
            g[fr].append(to)
            g[to].append(fr)
        
        #choose any node and run double dfs to get the diameter of the graph
        # running dfs on any node gauruntees finding one node of the 2 nodes that makes up the longest distance (diameter) of the graph
        path = [-1 for _ in range(n)]
        lst = [0 for _ in range(n)]
        dfs(0, lst, set(), 0, g)
        start = helper(lst)
        
        #reset lst
        for i in range(len(path)):
            path[i] = -1
            
        dfs(start, lst, set(), 0, g)
        end = helper(lst)
        mid = lst[end]//2
        ans = []
        # if diameter is odd (connecting even numbers of nodes), we take both nodes in the middle, otherwise we only need the middle node
        # reverse path traversal
        cur = end
        while path[cur] != -1:
            ans.append(cur)
            cur = path[cur]
        ans.append(start)
        return ans[mid:mid+2] if lst[end] % 2 else [ans[mid]]
        
        
        
        
            
        
        
        
        
        