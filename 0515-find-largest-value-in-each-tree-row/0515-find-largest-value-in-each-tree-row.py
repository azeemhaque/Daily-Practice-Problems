from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        max_result = []
        if not root:
            return max_result
        
        q = deque()
        q.append(root)   
        
        while q:
            max_val = float('-inf')
            for i in range (len(q)):
                node = q.popleft()
                max_val = max(max_val,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            max_result.append(max_val)
        return max_result
        