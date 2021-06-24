class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        result: accepted
        dp solution: specifics in the comments
        runtime: O(s*p), space: O(s*p)
        """
        mem = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        mem[0][0] = True
        for i in range(1, len(p)):
            #deals with empty string s cases
            mem[0][i+1] = mem[0][i-1] and p[i] == '*'
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == "*":
                    """
                    case1: mem[i][j] is True, ex(a, a*)
                    case2: mem[i+1][j-1] is True, ex(a, ac*)
                    case3:  ex(aa, a*)
                    """
                    mem[i+1][j+1] = mem[i+1][j-1] or mem[i+1][j] or (mem[i][j+1] and (s[i] == p[j-1] or p[j-1] == "."))
                else:
                    """
                    case1: mem[i][j] is True and s[i] == p[j] or p[j] == '.' ex(abc, ab.)
                    case2: mem[i+1][j-2] is True and p[j-1] == "*" ex(a, c*a)
                    """
                    mem[i+1][j+1] = (mem[i][j] or (j > 1 and p[j-1] == "*" and mem[i][j-2])) and (s[i] == p[j] or p[j] == ".")
        return mem[-1][-1]