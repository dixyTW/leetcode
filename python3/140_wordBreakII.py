class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        ans = []
        dic = set(wordDict)
        def dfs(i,lst,ans):
            if i == N:
                ans.append(" ".join(lst))
                return
            for word in dic:
                if s[i:i+len(word)] == word:
                    lst.append(word)
                    dfs(i+len(word),lst,ans)
                    lst.pop()
        dfs(0,[],ans)
        return ans
                