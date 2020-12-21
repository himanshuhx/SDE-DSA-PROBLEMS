class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, res):
            nonlocal ans
            if not len(nums):
                ans.append(res[:])
                # print(res)
                return
            for i in range(len(nums)):
                curr_char_choosen = nums[i]
                left_part_char = nums[:i]
                right_part_char = nums[i + 1:]
                left_over_nums = left_part_char + right_part_char
                res.append(curr_char_choosen)
                helper(left_over_nums, res)
                res.pop()

        ans = []
        helper(nums, [])
        return ans