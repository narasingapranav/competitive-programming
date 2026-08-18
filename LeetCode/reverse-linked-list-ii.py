# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy=ListNode(0,head)
        prev=dummy
        for i in range(left-1):
            prev=prev.next
        c=prev.next
        for i in range(right-left):
            temp=c.next
            c.next=temp.next
            temp.next=prev.next
            prev.next=temp
        return dummy.next