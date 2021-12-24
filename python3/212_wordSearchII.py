class Trie():
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word = None

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.word = word
class Solution: 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        initialize tree with words and try all paths (all paths that might lead to a word)
        """
        ans = []
        DIR = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c,t):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] not in t.children:
                return
            tmp = board[r][c]
            t = t.children[tmp]
            board[r][c] = "#"
            if t.word:
                ans.append(t.word)
                t.word = None #avoid dups, could use set for ans as well
            for x,y in DIR:
                dfs(r+x, c+y, t)
            board[r][c] = tmp
                
        root = Trie()
        for word in words:
            root.insert(word)
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,root)
        return ans
        