# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        queue = deque([(root1,root2)])

        
        while queue:
            r1, r2 = queue.popleft()
            r1.val += r2.val

            if r1.left and r2.left:
                queue.append((r1.left, r2.left))
            elif not r1.left and r2.left:
                r1.left = r2.left

            if r1.right and r2.right:
                queue.append((r1.right, r2.right))
            elif not r1.right and r2.right:
                r1.right = r2.right

        return root1
        