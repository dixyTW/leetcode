class Solution:
    def isValid(self, s: str) -> bool:
        """
        solution: accepted
        stack solution: 
        traverse the entire string 
        if we encounter an open parentheses, we place it on top of the stack
        if we encounter a closing parenthese, we take the parentheses on the top of the stack
        and compare if they match or not
        when we encounter an open parentheses we can only expect the following chars:
        1. another open parentheses 
        or 
        2. the closing parentheses
        anything else would cause a miss match in parentheses
        At the end of the loop, we check if the stack is empty to ensure that all
        opening parentheses are correctly matched
        runtime: O(n), space: O(n)
        """
        stack = [] 
        dic= {"(": ")", "{": "}", "[":"]"}
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if stack:
                    char = stack.pop()
                    if dic[char] != c:
                        return False
                else:
                    return False
        return not stack