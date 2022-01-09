class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
#         N = len(matrix)
#         dic = defaultdict(set)
#         for r in range(N):
            
#             s = set()
#             for c in range(N):
#                 dic[c].add(matrix[r][c])
#                 s.add(matrix[r][c])
#             for key in s:
#                 if key <= 0 or key > N:
#                     return False
#             if len(s) != N:
#                 return False
#         for n in dic:
#             for key in dic[n]:

#                 if key <= 0 or key > N:
#                     return False
#             if len(dic[n]) != N:
#                 return False 
        
#         return True
        n = len(matrix)
        for a, b in zip(matrix, zip(*matrix)):
            if len(set(a)) != n or len(set(b)) != n:
                return False
        return True