import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Outcome: Accepted
        naive solution: check every substring
        runtime: O(n^2), space: O(len(s)) for keeping track of the current string
        """
        # Max = 0
        # for i in range(len(s)):
        #     dic = set() #keep track of the current chars
        #     for j in range(i, len(s)):
        #         if s[j] in dic:
        #             #we can stop checking once we hit a duplicate char since
        #             #anything beyond this char is still a substring with dup char       
        #             break
        #         else:
        #             dic.add(s[j])
        #     Max = max(Max, len(dic))
        # return Max
        
        """
        Outcome: Accepted
        Sliding Window: keep left, right pointer. Left pointer for keeping track of 
        starting position, right pointer for traversing the string
        runtime: O(n), space: O(len(s))
        """
        if not s:
            return 0
        Max = 0
        l,r = 0,0
        dic = collections.defaultdict(int) #{char:index}
        for i, c in enumerate(s):
            r = i
            if c in dic:
                Max = max(Max, r-l)
                l = max(l,dic[c] + 1) #test case "abba", be careful of moving the left pointer
            dic[c] = i
        Max = max(Max, r-l+1)
        return Max