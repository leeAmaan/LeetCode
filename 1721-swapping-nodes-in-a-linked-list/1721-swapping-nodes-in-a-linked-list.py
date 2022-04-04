# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        # 투 포인터로 풀어보자
        # 값 지정해주기 
        slow, fast = head, head 
        
        # 1단계
        for _ in range(k-1):
            fast = fast.next
        first = fast
        
        # 2단계
        while fast.next:
            slow, fast = slow.next, fast.next
        
        # 3단계 
        first.val, slow.val = slow.val, first.val
        return head