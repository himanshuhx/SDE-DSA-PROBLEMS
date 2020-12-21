# approach 1
# aske interviewer for constraints suppose if ele>=0 always we choose -1 as flag
# whenever we encounter 0 we call setEle and set all ele of that col and row to -1 for later identification
# after whole array is traversed which is 0(n*m)
# we again traverse matrix and whenever we see ele = -1 this means this should be set to 0
# so set matrix[i][j]=0
# time complexity - (no of zeroes)*0(n+m) for updating to -1 every time + 0(n*m) for update traversal in original array
# + 0(n*m) for setting ele to 0
# space complexity 0(1)

class Solution:
    def setZeroes(self, nums: List[List[int]]) -> None:
        n = len(nums)
        m = len(nums[0])

        def setEle(i, j, nums, n, m):
            for k in range(n):
                nums[i][k] = -1
            for k in range(m):
                nums[k][j] = -1

        for i in range(n):
            for j in range(m):
                if nums[i][j] == 0:
                    setEle(i, j, nums, n, m)

        for i in range(n):
            for j in range(m):
                if nums[i][j] == -1:
                    nums[i][j] = 0

# approach 2 intuision is we maintain two sets namely rows and cols to mark up the index of rows and cols
# time complexity - 0(n*m) for storing indices in sets + 0(n*m) for updating
# space complexity 0(n) for two sets

class Solution:
    def setZeroes(self, nums: List[List[int]]) -> None:
        n = len(nums)
        m = len(nums[0])
        cols = set()
        rows = set()

        for i in range(n):
            for j in range(m):
                if nums[i][j] == 0:
                    cols.add(j)
                    rows.add(i)

        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    nums[i][j] = 0

# approach 3 recommended approach

class Solution:
    def setZeroes(self, nums: List[List[int]]) -> None:
        n = len(nums)
        m = len(nums[0])
        is0inFirstRow = False
        is0inFirstCol = False
        for i in range(m):
            if nums[0][i]==0:
                is0inFirstCol = True
        for j in range(n):
            if nums[j][0] == 0:
                is0inFirstRow = True
        for i in range(1,n):
            for j in range(1,m):
                if nums[i][j]==0:
                    nums[i][0]=0
                    nums[0][j]=0
        for i in range(1,n):
            if nums[i][0]==0:
                for j in range(1,m):
                    nums[i][j]=0
        for j in range(1,m):
            if nums[0][j]==0:
                for i in range(1,n):
                    nums[i][j]=0
        if is0inFirstRow:
            for i in range(n):
                nums[i][0]=0
        if is0inFirstCol:
            for j in range(m):
                nums[0][j]=0
