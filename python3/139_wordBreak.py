class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        result: AC
        runtime: O(N^2M), space: O(N)
        """
        # N = len(s)
        # dic = set(wordDict)
        # mem = [False for _ in range(N+1)] 
        # mem[0] = True
        # for i in range(1,N+1):
        #     for word in dic:
        #         if i >= len(word) and (s[i-len(word):i] in dic) and mem[i-len(word)]:
        #             mem[i] = True 
        # return mem[-1]
        
        """
        result: AC
        runtime: O(N^3)
        """
        N = len(s)
        dic = set(wordDict)
        mem = [False for _ in range(N+1)]
        mem[0] = True
        for i in range(1,N+1):
            for j in range(i):
                if mem[j] and s[j:i] in wordDict:
                    mem[i] = True
        return mem[-1]