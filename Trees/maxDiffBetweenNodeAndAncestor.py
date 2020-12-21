class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(root):
            nonlocal gmax
            if not root:
                return
            l = dfs(root.left)
            r = dfs(root.right)
            if not l and not r:
                return (root.val, root.val)
            mx, mn = float('-inf'), float('inf')
            if l:
                mx = max(l[0], mx)
                mn = min(l[1], mn)
            if r:
                mx = max(r[0], mx)
                mn = min(r[1], mn)
            gmax = max(gmax, abs(root.val - mx), abs(root.val - mn))
            return (max(mx, root.val), min(mn, root.val))

        gmax = 0
        dfs(root)
        return gmax