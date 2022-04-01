# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val: # 
                cur.next = cur.next.next # 중복된 노드 스킵
            cur = cur.next # 중복되지 않은 현재 노드 다음 노드로 이동
        return head