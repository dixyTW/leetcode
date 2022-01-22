class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def helper(w, s):
            if not s:
                return False
            N = len(w)
            mem = [False for _ in range(N+1)]
            mem[0] = True
            for i in range(1, N+1):
                for j in range(i):
                    if mem[j] and w[j:i] in s:
                        mem[i] = True
                        
            return mem[-1]
                    
        ans = []
        dic = set()
        words.sort(key=len) #sort by length, default sort by alphabetical order
        for word in words:
            if helper(word, dic):
                ans.append(word)
            dic.add(word)
        return ans