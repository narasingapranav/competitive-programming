# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict={}
        cur=head
        while cur:
            dict[cur.val] = dict.get(cur.val, 0) + 1
            cur=cur.next
        dummy=ListNode(0)
        cur=dummy
        node=head
        while node:
            if dict[node.val]==1:
                cur.next=ListNode(node.val)
                cur=cur.next
            node=node.next
        return dummy.next