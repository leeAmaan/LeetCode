# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 예외처리
        if not head or left == right:
            return head
        
        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(left-1):
            start = start.next
        end = start.next
        
        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
            
        