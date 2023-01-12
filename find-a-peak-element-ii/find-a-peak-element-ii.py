class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        mat = [[-1 for i in range(len(mat[0]) + 1)]] + [[-1] + row + [-1] for row in mat] + \
        [[-1 for i in range(len(mat[0]) + 1)]]

        def helper(left, right):
            if left >= right:
                print(left, right)
                newmat = [x[right] for x in mat]
                idx = newmat.index(max(newmat))
                return [idx, right]
            else:
                mid = left + (right - left)//2
                newmat = [x[mid] for x in mat]
                idx = newmat.index(max(newmat))

                if mat[idx][mid - 1] < mat[idx][mid] > mat[idx][mid + 1] and mat[idx-1][mid] < mat[idx][mid] > mat[idx+1][mid]: return [idx, mid]
                elif mat[idx][mid - 1] > mat[idx][mid]: return helper(left, mid - 1)
                else: return helper(mid + 1, right)
        res = helper(0, len(mat[0]))
        return [res[0] - 1, res[1] - 1]
