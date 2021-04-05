class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            nonlocal ans
            #print(ans)
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            ans = max(ans, left+right+root.val)
            return max(left+root.val,right+root.val,0)
        ans = -float("inf")
        helper(root)
        return ans