# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        temp=dummy
        while temp.next and temp.next.next:
            f=temp.next
            s=temp.next.next

            f.next=s.next
            s.next=f
            temp.next=s
            temp=f
        return dummy.next

