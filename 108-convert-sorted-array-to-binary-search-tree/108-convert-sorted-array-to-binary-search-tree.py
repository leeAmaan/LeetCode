# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        print(mid, "mid")
        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        print(node, "node")
        node.left = self.sortedArrayToBST(nums[:mid])
        print(node.left, "nodeleft")
        node.right = self.sortedArrayToBST(nums[mid+1:])
        print(node.right, "noderight")
        return node