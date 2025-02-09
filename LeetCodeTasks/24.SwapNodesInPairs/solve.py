class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    from typing import Optional
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy, dummy.next = ListNode(0), head
        current = dummy
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            first.next = current.next
            second.next = first
            current.next = second
            current = current.next.next
        return dummy.next
