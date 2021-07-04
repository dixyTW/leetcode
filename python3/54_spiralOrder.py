class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        result: accepted
        matrix manipulation: 
        step1: get the first row of the matrix
        step2: rotate the matrix counterclockwise 90 degrees
        repeat step 1 and 2 untill all elements are used
        
        """
        ans = []
        while matrix:
            ans += matrix.pop(0)
            matrix = list(zip(*[reversed(lst) for lst in matrix]))
        return ans 