# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def dfs(node):
            nonlocal max_len
            
            if node is None:
                return 0
            
            wide = 0
            current = 0
            
            if node.left:
                left = dfs(node.left)
                if node.left.val == node.val:
                    wide += 1 + left
                    current = max(current, 1+left)
            
            if node.right:
                right = dfs(node.right)
                if node.right.val == node.val:
                    wide += 1 + right
                    current = max(current, 1+right)
            
            max_len = max(max_len, wide, current)
            
            return current
        dfs(root)
        return max_len
            
   
        