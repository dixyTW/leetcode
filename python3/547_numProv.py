class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        g = defaultdict(list)
        N = len(isConnected)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if isConnected[i][j]:
                    g[i].append(j)
            if i not in g:
                g[i] = []
        visited = set()
        ans = 0
        for key in g:
            if key in visited:
                continue
            ans += 1
            lst = [key]
            while lst:
                nxt = lst.pop()
                if nxt not in visited:
                    for dest in g[nxt]:
                        visited.add(nxt)
                        lst.append(dest)
        return ans