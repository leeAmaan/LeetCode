# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
#         print(root.val)
#         print(root.right.right)
#         print(root.right.left.val)
        
#         # ans = []
        
#         # print(len(root)) 
#         # ans.append(root.val)
#         ans = [1,3,2] 
#         return ans 