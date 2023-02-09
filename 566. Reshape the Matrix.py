class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        def flatten(mat):
            return [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]

        def reshape(mat, r, c):
            if r*c != len(mat)*len(mat[0]): return mat
            arr = flatten(mat)
            return list([arr.pop(0) for j in range(c)] for i in range(r))
        
        return reshape(mat, r, c)