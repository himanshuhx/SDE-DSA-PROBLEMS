# https://www.youtube.com/watch?v=mMVCcTBqnrs

def symmetric(root):
    def helper(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if right.val==left.val:
            return helper(left.left, right.right) and helper(left.right,right.left)
        else:
            return False

    return True if not root else helper(root.left, root.right)