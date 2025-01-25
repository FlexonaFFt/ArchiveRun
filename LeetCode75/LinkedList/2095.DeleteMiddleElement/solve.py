class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    from typing import Optional
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow, prev = head, head, None
        if not head or not head.next:
            return None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head
