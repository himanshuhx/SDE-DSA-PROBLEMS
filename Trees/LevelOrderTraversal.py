from collections import deque
class Solution:
    def levelOrderTraversal(self,root):
        queue = deque()
        queue.append(root)
        levelOrder = []
        while queue:
            for i in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queu.append(node.right)
            level.append(curr_node.val)
        return levelOrder