# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # n ahead
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        
        
        
        
        # index and remove
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i + 1, (head, head.next)[i+1 == n]
        #return remove(head)[1]
        
        
        # value-shifting
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            print(i, "i") 
            if i > n:
                node.next.val = node.val
                print(node.next.val, "node.next.val")
            return i
        #index(head)
        #return head.next
        
        #head.next, prev = 
        #prev