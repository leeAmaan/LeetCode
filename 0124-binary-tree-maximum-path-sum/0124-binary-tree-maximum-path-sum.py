# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        def max_sum(node):
            if not node:
                return [-2**31] * 2
            left = max_sum(node.left)
            right = max_sum(node.right)
            return [node.val + max(left[0], right[0], 0), max(left+right+[node.val+left[0]+right[0]])]
        
        #print(max_sum(root))
        return max(max_sum(root))
        
        
        
        