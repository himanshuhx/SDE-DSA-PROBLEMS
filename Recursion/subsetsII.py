# find all the subsets without any duplicates

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(nums,res,path):
            res.append(path)
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                helper(nums[i+1:],res,path+[nums[i]])
        res = []
        nums.sort()
        helper(nums,res,[])
        return res