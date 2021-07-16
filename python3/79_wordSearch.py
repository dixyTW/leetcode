class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        result: AC
        dfs backtrack
        runtime: O(m*n*3^k) (3 not 4 because we cant go back), space: O(mn)
        """
        def helper(r, c, i, seen):
            if len(word) == i:
                return True
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and (r,c) not in seen and board[r][c] == word[i]:
                res = False
                seen.add((r,c))
                for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                    res |= helper(r+y, c+x, i+1, seen)
                seen.remove((r,c))
                return res
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if helper(r,c,0,set()):
                        return True
        return False