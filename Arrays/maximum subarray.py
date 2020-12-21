# Kadanes algo 0n time 01 space
# intusion as soon as we hit the value of sum<0 update it to sum=0

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            maxSum = max(maxSum, sum)
            if sum<0:
                sum=0
        return maxSum