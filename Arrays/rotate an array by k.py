# reverse whole array -> reverse first half -> reverse second half
class Solution:
    def rotate(self, nums, k: int) -> None:
        def reverse(low, high):
            while low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

        n = len(nums)
        k = k % n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


class Solution:
    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        n[:] = nums[:n-k] + nums[k:n-1]