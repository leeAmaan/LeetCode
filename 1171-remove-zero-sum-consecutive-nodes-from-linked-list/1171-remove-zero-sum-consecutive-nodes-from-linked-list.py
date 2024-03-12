# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:   
#     def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         head_list = []
#         current_node = head
#         while current_node is not None:
#             head_list.append(current_node.val)
#             current_node = current_node.next

            
            
            
class Solution:
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prefixSumToNode = {}
        prefixSum = 0
        current = dummy
        while current:
            prefixSum += current.val
            if prefixSum in prefixSumToNode:
                prev = prefixSumToNode[prefixSum]
                toRemove = prev.next
                p = prefixSum + (toRemove.val if toRemove else 0)
                while p != prefixSum:
                    del prefixSumToNode[p]
                    toRemove = toRemove.next
                    p += toRemove.val if toRemove else 0
                prev.next = current.next
            else:
                prefixSumToNode[prefixSum] = current
            current = current.next
        return dummy.next            
            
            #         ls1 = head_list
#         ls2 = head_list
#         ans1 = []
#         ans2 = []
#         for i in range(len(head_list)):
#             ans1.append(ls1.pop())
#             if sum(ls1) == 0:
#                 return ans1 
        
#         for j in range(len(head_list)):
#             ans2.append
#             if sum  == 0:
        