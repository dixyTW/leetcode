class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sort
        # N = len(citations)
        # citations.sort()
        # ans = 0
        # for i, h in enumerate(citations):
        #     if h >= N-i:
        #         return N-i
        # return 0
        
        dic = Counter(citations)
        l, r = min(citations), max(citations)
        i = 0
        N = len(citations)
        while l <= r:
            while l in dic and dic[l] != 0:
                if l >= N-i:
                    return N-i
                i += 1
                dic[l] -= 1
            l += 1
        return 0 
        