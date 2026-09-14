# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=set()
        current=head
        previous=None
        while current:
            if current.val in a:
                previous.next=current.next
            else:
                a.add(current.val)
                previous=current
            current=current.next
        return head