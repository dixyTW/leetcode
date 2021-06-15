class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        result: accepted
        pattern observed:
        if c is (
        1. there could be subsequent ) that completes the parenthesis
        2. could block previous completed substrings
        if c is )
        1. if opening parentheses, completes the parenthesis, 
        2. if there's no remaining opening parentheses, indicator for breaking the valid parentheses substring.
        stack solution:
        each 0 in the stack represents an open parentheses
        when we encounter a closing parentheses, if the stack is not empty,
        we pop the stack, and put the value back into the top of the stack
        stack is initialized to [0] to deal with special case "()" to make the algorithm consistent
        runtime: O(n), space: O(n)
        
        Think of a desired behavior (representation) of your algorithm, and try to tweek your code
        to match that behavior
        """
        stack = [0] #initiazlie with 0 to handle the first valid parentheses
        Max = 0
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) <= 1:
                    #means empty 
                    stack = [0]
                else:
                    val = stack.pop()
                    stack[-1] += val+2
                    Max = max(Max, stack[-1])
        return Max