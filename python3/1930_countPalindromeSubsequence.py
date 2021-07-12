class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        result: accepted
        initial attempt: 3 word palindrome are formed with the same character 
        left and right and any character in the middle
        We get position of left most and right most of the same character, and count the number of characters         within the two characters, while keeping track of duplicates
        runtime: worst case "abcdefggfedcba", if the string keeps triggering the helper function. 
                 n + n-2 + n-4 ... 2 -> O(n^2), space(n)
        """
        # def helper(l,r):
        #     for i in range(l+1, r):
        #         if (s[l], s[i], s[r]) not in seen:
        #             self.ans += 1
        #             seen.add((s[l], s[i], s[r]))
        # seen = set() 
        # self.ans = 0
        # dic = collections.defaultdict(list)
        # for i, c in enumerate(s):
        #     dic[c].append(i)
        # for key in dic:
        #     if len(dic[key]) > 1:
        #         lst = dic[key]
        #         helper(lst[0],lst[-1])
        # return self.ans
        res = 0
        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1: j]))
        return res