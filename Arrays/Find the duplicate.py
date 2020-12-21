# approach 1 - sorting and than finding the duplicate 0(nlogn),0(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

# approach 2 using map/frequency array and keeping track of count/ele visited 0N time 0N space

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = set()
        for num in nums:
            if num in map:
                return num
            else:
                map.add(num)

# approach 3 Hare and Tortoise method 0N time 01 space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow