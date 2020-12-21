'''

 brute force 0(n^2) 0(1)  counting each ele occurence in two loops and checking for count>n//2

 Hashmap approach 0(n) 0(n) keeping count in hashmap and checking count

 Optimal approach - moore's algo - initialize countt =0 and curr_ele = nums[0]
 iterate over nums if next ele is same count++ else count--
 if count == 0 update curr_ele to nums[i]
 return ele (ans)
 Time - 0(n) space - 0(1)

'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        ele = nums[0]
        for i in range(n):
            if not count:
                ele = nums[i]
            if nums[i] == ele:
                count += 1
            else:
                count -= 1
        return ele