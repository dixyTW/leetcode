class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        result: TLE
        brute force dfs: try every possible combination
        runtime: O(2^n)
        """
        # def helper(one, two, thr):
        #     if not one and not two and not thr:
        #         return True
        #     if (one or two) and thr:
        #         res = False
        #         if one and one[0] == thr[0]:
        #             res |= helper(one[1:], two, thr[1:])
        #         if two and two[0] == thr[0]:
        #             res |= helper(one, two[1:], thr[1:])
        #         return res
        #     else:
        #         return False
        # return helper(s1, s2, s3)
        """
        result:
        memoization dfs
        runtime: O(mn)
        """
        # @lru_cache
        # def helper(i1, i2, i3):
        #     if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
        #         return True
        #     if (i1 < len(s1) or i2 < len(s2)) and i3 < len(s3):
        #         res = False
        #         if i1 < len(s1) and s1[i1] == s3[i3]:
        #             res |= helper(i1+1, i2, i3+1)
        #         if i2 < len(s2) and s2[i2] == s3[i3]:
        #             res |= helper(i1, i2+1, i3+1)
        #         return res
        #     else:
        #         return False
        # return helper(0,0,0)
        """
        result: AC
        DP
        runtime: O(mn)
        """
        if len(s1) + len(s2) != len(s3):
            return False 
        mem = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        mem[0][0] = True
        for i in range(len(s1)):
            mem[i+1][0] = (s1[i] == s3[i] and mem[i][0])
        for j in range(len(s2)):
            mem[0][j+1] = (s2[j] == s3[j] and mem[0][j])
        for i in range(len(s1)):
            for j in range(len(s2)):
                mem[i+1][j+1] = (mem[i][j+1] and s1[i] == s3[i+j+1]) or (s2[j] == s3[i+j+1] and mem[i+1][j])
        return mem[-1][-1]
    