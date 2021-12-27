class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        dic = set(spaces)
        i = 0
        while i < len(s):
            if i in dic:
                ans.append(" ")
                dic.remove(i)
            else:
                ans.append(s[i])
                i += 1
            
        return "".join(ans)