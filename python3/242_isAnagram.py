class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #need to check if both words contains exactly the same characters
        dic = collections.defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            if not dic[c]:
                return False
            else:
                dic[c] -= 1
        for key, val in dic.items():
            #case ab, a
            if val >= 1:
                return False
        return True