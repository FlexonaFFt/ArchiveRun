class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return None        
        val_toremove = set(nums)
        while head and head.val in val_toremove:
            head = head.next 

        current = head
        while current.next:
            if current.next.val in val_toremove:
                current.next = current.next.next
            else: current = current.next
        return head 
