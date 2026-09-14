# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k<=1:
            return head
        def has_k_nodes(node):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while has_k_nodes(prev.next):
            curr = prev.next
            nxt = curr.next
            for _ in range(k - 1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            prev = curr
        return dummy.next