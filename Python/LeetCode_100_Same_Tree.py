# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p == None and q == None:
            return True

        if p == None or q == None: # 在左右不確定哪個是空的情況之下
            return False
        
        if p.val != q.val : # 值不相等
            return False

        resultL = self.isSameTree(p.left, q.left)
        resultR = self.isSameTree(p.right, q.right)

        return resultL and resultR