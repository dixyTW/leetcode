class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        """
        https://leetcode.com/problems/largest-number-after-mutating-substring/discuss/1362174/Python-Greedy-Solution-with-Thought-Process
        runtime: O(n^2)
        """
        ans = ""
        b = False
        for i, n in enumerate(num):
            if b:
                if int(n) > change[int(n)]:
                    ans += num[i:]
                    break
                else:
                    ans += str(change[int(n)])
            else:
                if int(n) < change[int(n)]:
                    b = True
                    ans += str(change[int(n)])
                else:
                    ans += n 
        return ans