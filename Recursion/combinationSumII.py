# Two patterns are there two solve most of the problems regarding recurdion with arrays
# pick and non pick method(CombinationSum 1) and other is (combinationSum 2)
# in CS 2 we are skipping the indx if duplicate ele
# One imp point - in cases like where we have to add some ds to our final answer
# check for backtracking and use ds.pop() to remove the last ele while coming back fro recursion.

class Solution(object):
    def combinationSum2(self, candidates, target):
        def helper(idx,target,ds):
            if target==0:
                res.append(ds[:])
                return
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if target>=candidates[i]:
                    ds.append(candidates[i])
                    helper(i+1,target-candidates[i],ds)
                    ds.pop()
        candidates.sort()
        res = []
        helper(0,target,[])
        return res