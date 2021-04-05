class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def helper(target, idx, arr, ds):
            if idx == len(arr):
                if target == 0:
                    res.append(ds[:])
                return
            if arr[idx] <= target:
                ds.append(arr[idx])
                helper(target - arr[idx], idx, arr, ds)
                ds.pop()
            helper(target, idx + 1, arr, ds)

        helper(target, 0, candidates, [])
        return res
