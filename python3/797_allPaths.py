class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        edge cases:
        1. cycles
        2. is there always a path from src -> dest
        """
        self.ans = []
        n = len(graph) - 1
        def dfs(cur, path):
            if cur == n:
                newans = copy.deepcopy(path)
                self.ans.append(newans)
                return
            for nxt in graph[cur]:
                path.append(nxt)
                dfs(nxt, path)
                path.pop()
            
        dfs(0, [0])
        return self.ans
            
        