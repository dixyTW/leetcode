class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        result: accepted
        traverse backwards: 
        for each itteration, always do the same thing.
        1. Keep track of the carry bit and update digits
        runtime: O(n), space: O(1)
        """
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)
        if carry:
            digits = [1] + digits
        return digits