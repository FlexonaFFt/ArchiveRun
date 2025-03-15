from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime 116 ms, 86.64 %
# Memory 60.51 mb, 66.02 %
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next
        next_sum = modify
        while next_sum:
            total = 0
            while next_sum.val != 0:
                total += next_sum.val
                next_sum = next_sum.next
            modify.val = total
            next_sum = next_sum.next
            modify.next = next_sum
            modify = modify.next
        return head.next
