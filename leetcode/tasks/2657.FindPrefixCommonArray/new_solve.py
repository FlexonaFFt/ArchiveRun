from typing import List 

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)
        common_array = [0] * n 

        for current in range(n):
            common_counter = 0 

            for a_index in range(current + 1):
                for b_index in range(current + 1):
                    if A[a_index] == B[b_index]:
                        common_counter += 1
                        break 

            common_array[current] = common_counter
        return common_array
