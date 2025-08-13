from collections import deque
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
        stack = [(root, 1)] # 初始化陣列
        max_depth = 0
        if root is None:
            return max_depth
        
        while stack:
            node, depth = stack.pop()
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth +1))
            max_depth = max(max_depth, depth)
        return max_depth