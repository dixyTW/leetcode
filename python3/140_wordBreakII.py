class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        wordSet = set(wordDict)
        mem = [[] for _ in range(N)]
        def dfs(i):
            
            if i == N:
                return [""]
            if mem[i]:
                return mem[i]
            for j in range(i+1, N+1):
                cur = s[i:j]
                if cur in wordSet:
                    res = dfs(j) 
                    if res:
                        for w in res:
                            newWord = cur + ("" if w == "" else " ") + w
                            mem[i].append(newWord)
            return mem[i]

        dfs(0)
        return mem[0]
        
        
        
        """
        N = len(s), M = len(wordDict)
        runtime: (MN)^N (absolute worst, not possible due to testcase constraint)
        """
#         N = len(s)
#         ans = []
#         dic = set(wordDict)
#         def dfs(i,lst,ans):
#             if i == N:
#                 ans.append(" ".join(lst))
#                 return
#             for word in dic:
#                 if s[i:i+len(word)] == word:
#                     lst.append(word)
#                     dfs(i+len(word),lst,ans)
#                     lst.pop()
#         dfs(0,[],ans)
#         return ans
        
        
        
                