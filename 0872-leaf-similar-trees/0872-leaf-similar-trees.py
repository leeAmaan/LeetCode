# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        return self.leaf(root1) == self.leaf(root2)
        
#         if not root1:
#             return []
#         if not root2:
#             return []
#         if not (root1.left or root1.right):
#             return [root1.val]
#         if not (root2.left or root2.right):
#             return [root2.val]
        
#         if self.leafSimilar(root1.left, root1.right) == self.leafSimilar(root2.left, root2.right):
#             return True
#         else:
#             return False
        
    def leaf(self, root):
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]
        return self.leaf(root.left)+self.leaf(root.right)
        
        