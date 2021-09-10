class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            fr, to = edges[i]
            graph[fr].append((to, succProb[i]))
            graph[to].append((fr, succProb[i]))
        succ = [0 for _ in range(n)]
        h = [(-1, start)]
        while h:
            prob, cur = heappop(h)
            prob = -prob
            for nxt, p in graph[cur]:
                if prob*p > succ[nxt]:
                    succ[nxt] = prob*p
                    heappush(h, (-succ[nxt], nxt))
        return succ[end]
            