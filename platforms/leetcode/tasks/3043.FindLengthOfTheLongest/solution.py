from typing import List 

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        array1, last = set(), 0
        for value in arr1:
            while value not in array1 and value > 0:
                array1.add(value)
                value //= 10 

        for value in arr2:
            while value not in array1 and value > 0:
                value //= 10
            if value > 0:
                last = max(last, len(str(value)))

        return last
