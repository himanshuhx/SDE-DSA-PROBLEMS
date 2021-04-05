# Approach - Sort the start and end arr
# using while loop as if start[i]>end[j] -> we dont need to increment i only increment j...this was the problem
# with for loop that gives WA
# Time complexity O(nlogn)+O(nlogn)+O(2*n)


class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, start, end):
        start.sort()
        end.sort()
        ans, i, j, platform = 1, 1, 0, 1
        while i < n and j < n:
            if start[i] <= end[j]:
                platform += 1
                i += 1

            elif start[i] > end[j]:
                j += 1
                platform -= 1
            ans = max(ans, platform)
        return ans