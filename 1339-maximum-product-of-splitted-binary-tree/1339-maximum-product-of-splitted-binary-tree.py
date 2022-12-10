# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        vals = []
        
        def tree_sum(node):
            if not node:
                return 0
            ans = node.val + tree_sum(node.left) + tree_sum(node.right)
            vals.append(ans)
            return ans
        
        total = tree_sum(root)
        return max((total - x)*x for x in vals)%(10**9 + 7)