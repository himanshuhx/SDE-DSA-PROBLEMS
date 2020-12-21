class Solution:
    def searchRange(self, nums, target: int) :
        def leftSearch(nums, n, target):
            nonlocal left
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    left = mid
                    high = mid - 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return left

        def rightSearch(nums, n, target):
            nonlocal right
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    right = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return right

        left, right = -1, -1
        leftSearch(nums, len(nums), target)
        rightSearch(nums, len(nums), target)
        return [left, right]
