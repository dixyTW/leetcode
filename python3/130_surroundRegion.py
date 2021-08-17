class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        result: AC
        dfs: the only case where we don't convert "O" to "X" is when "O" is on the border of the         board. Using this idea, if we traverse the board from the boarder, the path of that               starts from the border with "O" will remain "O"
        runtime: O(MN), space: O(1)
        """
        M, N = len(board), len(board[0])
        def dfs(r,c):
            if 0 <= r < M and 0 <= c < N:
                if board[r][c] != "O":
                    return
                board[r][c] = "T"
                for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    dfs(r+y, c+x)
                    
        for i in range(M):
            dfs(i,0)
            dfs(i,N-1)
        
        for i in range(N):
            dfs(0, i)
            dfs(M-1, i)
        
        for r in range(M):
            for c in range(N):
                board[r][c] = "X" if board[r][c] != "T" else "O"
                