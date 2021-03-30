# Naive Approach
# Get the maxLeft and maxRight at every ith index
# res += min(maxLeft,maxRight) - a[i]
# Time Complexity - O(N)*(O(N)+O(N))  Space Complexity - O(1)
# O(N) --> To iterate over every index
# O(N)+O(N) --> to get maxL and MaxRight

# Approach 2 (Using Extra space to store maxL and MaxR at every index)
# Time Complexity - O(N)+O(N)+O(N) Space Complexity - O(2*N)
class Solution:
    def trap(self, arr: List[int]) -> int:
        if not arr:
            return 0
        n = len(arr)
        pre, suff = [0]*n, [0]*n
        maxL, maxR = arr[0], arr[-1]
        for i in range(n):
            maxL = max(maxL, arr[i])
            pre[i] = maxL
        for i in range(n-1,-1,-1):
            maxR = max(maxR, arr[i])
            suff[i] = maxR
        res = 0
        for i in range(n):
            res += min(pre[i], suff[i]) - arr[i]
        return res



# Optimized Approach
# Two Pointer Approach
# Time Complexity - O(N) Space Complexity - O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        res = 0
        maxLeft, maxRight = 0, 0

        while left <= right:

            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res