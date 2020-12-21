class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def helper(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            elif i > m - 1 or j > n - 1:
                return 0
            else:
                return helper(i + 1, j) + helper(i, j + 1)

        return helper(0, 0)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i > m - 1 or j > n - 1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = helper(i + 1, j) + helper(i, j + 1)
            return dp[i][j]

        dp = [[-1] * n] * m
        return helper(0, 0)


from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))
