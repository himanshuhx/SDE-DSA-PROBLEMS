# approach 1 just sort the array 0(nlogn) 01

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()

# approach 2 maintaining count of 0 1 and 2
# thAN COPYING 0 1 AND 2 ACCORDING TO COUNT IN OORIGINAL ARRAY
# TWO PASSES REQUIRED 0n TIME 01 SPACE

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0=count1=count2=0
        for num in nums:
            if num==0:
                count0 += 1
            elif num==1:
                count1 += 1
            else:
                count2 += 1
        i=0
        while True:
            if i>=len(nums):
                break
            if count0:
                nums[i]=0
                count0 -= 1
            elif count1:
                nums[i] = 1
                count1 -= 1
            else:
                nums[i] = 2
                count2 -= 1
            i+=1

# approach 3 ud=sing 3 pointers low, mid and high
# 0N time 01 space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
