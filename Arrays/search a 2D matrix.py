'''
four approaches are there

 approach 1 - simply do a linear search to find the target element
 Time - 0(n^2) Space - 0(1)

 approach 2 - use an axtra 1d array of size n*m
 step 1 - copy all the ele from original to temp 1d arr
 step 2 - do a binary search on temp arr
 Time - 0(n^2) + 0(logn) Space - 0(n*m)

 approach 3 - ask the interviewer if rows and col both are sorted if it,
 than
 step 1 - start from first row last col index
 step 2 - if target > currIndexEle move bottom else move left
 step 3 - do this until we hit the target element or we run out of bounds

 approach 4 - the most optimal approach
 intusion - think of converting the 2d array in 1d array , how to do that?
 well idea is simple ( mid//m = i , mid%m = j ) where n,m = len(matrix), len(matrix[0])
 and do the binary search
 Time - 0(log(n*m)) since we are doing a binary search on length (n*m) , Space - 0(1)

'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        n = len(matrix)
        m = len(matrix[0])

        low, high = 0, (n * m) - 1

        while low <= high:

            mid = (low + high) // 2

            if matrix[mid // m][mid % m] == target:
                return True
            if matrix[mid // m][mid % m] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False