# conclusions
# in pascals triangle 1 and 2 rows are always filled with 1
# 1st and last ele of a row is always 1
# ele at i,j index is sum of prev row i-1,j and i-1,j-1 index
# ele at i,j index is iCj or at row,col = row-1 C col-1

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        arr = [[1]*(i+1) for i in range(n)]
        for i in range(2,n):
            for j in range(1,i):
                 arr[i][j] = arr[i-1][j]+arr[i-1][j-1]
        return arr