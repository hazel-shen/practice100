# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth = 0
        if root == None:
            return 0
        depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        return depth
