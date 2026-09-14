# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, List1: Optional[ListNode], List2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        while List1 and List2:
            if List1.val < List2.val:
                tail.next=List1
                List1=List1.next
            else:
                tail.next=List2
                List2=List2.next
            tail=tail.next
        tail.next= List1 if List1 else List2
        return dummy.next