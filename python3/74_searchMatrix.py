class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        result: accepted
        binary search: first binary search the correct row, then binary search the column
        runtime: O(log(m*n)) #worst case the matrix is a list, space: O(1) 
        """
        row = -1
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    row = mid
                    break
                else:
                    l = mid+1
        
        if row == -1:
            return False
        
        l, r = 0, len(matrix[0])-1
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False 