class Solution:
    from typing import List
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for element in nums1:
            if element == 0:
                nums1.remove(element)
        for element in nums2:
            nums1.append(element)
        nums1.sort()

# Это решение не проходит все тесты
