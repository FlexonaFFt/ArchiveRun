class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 


from typing import Optional
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int: 
        result, current = 0, head 

        while current:
            result = (result << 1) | current.val 
            current = current.next 

        return result 

