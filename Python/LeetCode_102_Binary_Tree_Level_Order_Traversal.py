# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        temp_queue = deque([root])
        all_queue = []
        if root is None:
            return all_queue
        
        while temp_queue:
            length = len(temp_queue)
            buffer_queue = []
            for _ in range(length):
                node = temp_queue.popleft()
                buffer_queue.append(node.val) # 把這層的值存到一個暫存的list
                if node.left is not None:
                    temp_queue.append(node.left) # 儲存下一層的值
            
                if node.right is not None:
                    temp_queue.append(node.right)  # 儲存下一層的值
            all_queue.append(buffer_queue)  # 把這層的值先倒出來

        return all_queue
