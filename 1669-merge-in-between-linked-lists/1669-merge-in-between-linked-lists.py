# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp1=list2
        head=list1
        pos=list2
        end=list1
        while list2.next:
            list2=list2.next
        i,j=0,0
        while list1:
            if i==a-1:
                pos=list1
            if j==b:
                end=list1
            i+=1
            j+=1
            list1=list1.next
        pos.next=temp1
        list2.next=end.next
        return head