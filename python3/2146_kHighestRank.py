class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        direct = [(1,0),(-1,0),(0,1),(0,-1)]
        M, N = len(grid), len(grid[0])
        q = deque([(start[0], start[1], 0)])
        dist_grid = [[-1 for _ in range(N)] for _ in range(M)]
        visited = set()
        visited.add((start[0], start[1]))
        ranking = []
        while q:
            r, c, dist = q.popleft()
            dist_grid[r][c] = dist
            for x, y in direct:
                new_r, new_c = r+x, c+y
                if 0 <= new_r < M and 0 <= new_c < N and grid[new_r][new_c] != 0 and (new_r, new_c) not in visited:
                    q.append((new_r, new_c, dist+1))
                    visited.add((new_r,new_c))
        
        for r in range(M):
            for c in range(N):
                if pricing[0] <= grid[r][c] <= pricing[1] and dist_grid[r][c] != -1:
                    ranking.append([dist_grid[r][c], grid[r][c], r, c])
        
        ranking.sort(key=lambda x: [x[0], x[1], x[2], x[3]])
        ans = [[item[2], item[3]] for item in ranking[:k]]
        return ans 
        
                    
                
        
        