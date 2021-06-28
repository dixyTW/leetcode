class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        result: accepted
        stack solution: while iterating through the string, 
        push the chars into a stack and check if the top of the stack contains the part str, 
        remove all instances of the part str within the stack before moving on to the next char
        the stack now only contains chars that does not contain the part str
        runtime: O(n), space: O(n)
        """
        stack = []
        i = 0
        leng = len(part)
        while i < len(s):
            stack.append(s[i])
            i += 1
            while len(stack) >= leng and ''.join(stack[-leng:]) == part:
                for _ in range(leng):
                    stack.pop()
        return ''.join(stack)
                