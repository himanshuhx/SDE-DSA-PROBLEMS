# Logic  - assigning a range [min,max] node val should be min<node.val<max

def isBst(root):
    def helper(root, min, max):
        if not root:
            return True
        return (min<root.val and max>root.val and helper(root.left,min,root.data) and helper(root.right,root.data,max))

    min = -float('inf')
    max = float('inf')
    return helper(root,min,max)

# Logic - a bst always produces inorder in sorted format

 def isBst(root):
    def isInorder(root):
        if not root:
            return True
        if not isInorder(root.left):
            return True
        if prev>=root.val:
            return False
        prev = root.val
        return isInorder(root.right)

    min = -float('inf')
    return isInorder(root)