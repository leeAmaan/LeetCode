# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            #print(p, "p1")
        # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            #print(head.next, "head.next")
            p.next = head
            #print(p.next, "p.next")
            return p
            #print(p, "return p")
        return head
        
        
        
        
        
        
        #root = prev = ListNode(None)
        #prev.next = head
        #print(head.next)
        #print(prev.next)
        #while head and head.next:
            # print(head, head.next)
            # b가 a(head)를 가리키도록 할당
         #   b = head.next
          #  print(b)
          #  print(head, "head1")
          #  head.next = b.next
          #  print(head.next)
          #  print(head, "head2")
          #  b.next = head
          #  print(b.next)
           # print(head, "head3")
            
            # prev가 b를 가리키도록 할당
            #prev.next = b
            #print(prev.next)
            # 다음번 비교를 위해 이동 
            #head = head.next
            #prev = prev.next.next
            #print(prev)
        #return root.next
            
        
        
        

        