# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head 
        
        while cur and cur.next:
            # 값만 교환 
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
            
        return head
        
        
        
        
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            print(head.next)
            p.next = head
            return p 
        return head
        