'''

 approach 1 - Brute Force two loops over the array and check count>n//3
            Time - 0(n^2) Space - 0(1)

 approach 2 - Use HashMap to store the count
              Time - 0(n) or 0(nlogn) depends upon map Space - 0(1)

 approach 3 - Moore's voting algo (extended version)
              two variables number1, number2 and two variables to keep their count track count1, count2
              Number of majority elements can lie in range [0,2] as count should be floor(n/3)

'''


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        number1, number2, count1, count2 = -1, -1, 0, 0
        for i in range(len(nums)):
            if number1 == nums[i]:
                count1 += 1
            elif number2 == nums[i]:
                count2 += 1
            elif count1 == 0:
                number1 = nums[i]
                count1 += 1
            elif count2 == 0:
                number2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        ans = []
        for i in range(len(nums)):
            if nums[i] == number1:
                count1 += 1
            elif nums[i] == number2:
                count2 += 1
        if count1 > len(nums) // 3:
            ans.append(number1)
        if count2 > len(nums) // 3:
            ans.append(number2)
        return ans
