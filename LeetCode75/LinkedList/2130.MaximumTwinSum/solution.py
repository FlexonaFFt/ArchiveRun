class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

class Solution:
    from typing import Optional
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = reverseList(slow)
        max_sum = float('-inf')
        first_half = head
        while second_half:
            current_sum = first_half.val + second_half.val
            max_sum = max(max_sum, current_sum)
            first_half = first_half.next
            second_half = second_half.next
        return max_sum
