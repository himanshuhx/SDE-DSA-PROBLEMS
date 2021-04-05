# https://practice.geeksforgeeks.org/problems/subset-sums2234/1#

class Solution:
	def subsetSums(self, arr, N):
	    def helper(idx, sum, arr, n, res):
            if idx==n:
                res.append(sum)
                return
            helper(idx+1, sum+arr[idx], arr, n, res)
            helper(idx+1, sum, arr, n, res)
		res = []
		helper(0, 0, arr, N, res)
		res.sort()
		return res