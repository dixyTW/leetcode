class Solution:
    def minSwaps(self, s: str) -> int:
        """
        runtime: O(n), space: O(n)
        """
        stack = []
        comp = 0
        for c in s:
            if c == "[":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                    comp += 1 
        return math.ceil(((len(s) - comp*2)/2)/2)
        