# approach transpose -> reverse col

class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            low = 0
            high = n - 1
            while low < high:
                matrix[i][low], matrix[i][high] = matrix[i][high], matrix[i][low]
                low += 1
                high -= 1